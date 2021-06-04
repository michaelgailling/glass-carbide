# Project Name:
# Glass Carbide
#
# By:
# Michael Gailling
# &&
# Mustafa Butt
#
# Organization:
# WIMTACH
#
import asyncio
import json
from datetime import datetime
import sys
from math import floor

from PySide2.QtCore import Qt, QThreadPool, Slot
from PySide2.QtWidgets import QApplication, QFrame, QVBoxLayout, QHBoxLayout, QPushButton

from GC_Components.InputComponents import LabeledInputWithButton
from GC_Components.TableComponents import DataTable, SimpleDataTable
from GC_Services.FileIo import FileIo
from GC_Services.pcloudAPI import PCloud
from GCFileDetailsView import FileDetailsView
from GC_Threading.Worker import DownloadWorker


class GCResultsOutputView(QFrame):
    """Results Output View

        Summary:
            A class for viewing results of CSV selection & searching/downloading results on pcloud that includes:

            -Data Table of selected results to the top left
            -Data Table of selected filenames from results
            -Data Table of added pcloud links
            -VBox with LabeledInputWithButton for adding pcloud links & buttons for scanning & downloading from pcloud

        Attributes:
            parent, shot_data, filenames, file_metadata, publinks, cloud_scanned, fio, apic, threadpool, hbl_tables,
            dt_shot_data, dt_files, hbl_controls, dt_cloud_links, liwb_add_publink, vbl_control_buttons, btn_scan,
            btn_download_files, vbl_main_layout

        Methods:
            add_publink_clicked, scan_pcloud_clicked, download_files_clicked, load_shot_table_data, load_filename_table,
            add_publink_to_table, get_codes, search_for_files, get_publink_data, classify_files, color_filename_cells,
            color_shot_table, get_matching_files, find_latest_file, download_files, update_progress_bar, test_popup,
            download_finished, create_unique_filename_list, set_shot_data

        Attributes
        ----------
            parent : QFrame
                Parent QFrame
            shot_data : []
                Array for selected data from table view
            filenames : []
                Array of selected asset listings/filenames
            file_metadata : []
                Array for metadata for selected files
            publinks : []
                Array for user-inputted publinks
            cloud_scanned : bool
                Bool for whether pCloud scan successful
            fio : FileIo
                File input & output
            apic : PCloud
                PCloud API class
            threadpool : QThreadPool
                Threadpool for multithreading threads
            hbl_tables : QHBoxLayout
                HBox layout for tables
            dt_shot_data : DataTable
                Data Table for selected columns and rows
            dt_files : SimpleDataTable
                Data Table for selected assets
            hbl_controls : QVBoxLayout
                VBox layout for pCloud buttons
            dt_cloud_links : SimpleDataTable
                Data Table for publinks
            liwb_add_publink : LabeledInputWithButton
                Labeled Input With Button for pCloud/publink access
            vbl_control_buttons : QVBoxLayout
                Vertical layout for control buttons
            btn_scan : QPushButton
                Button for scanning PCloud
            btn_download_files : QPushButton
                Button for downloading selected files from PCloud
            vbl_main_layout = QVBoxLayout
                Main VBox layout

        Methods
        -------
            add_publink_clicked(self)
                Adds publink to dt_cloud_links table when Add Link button clicked
            scan_pcloud_clicked(self)
                Checks pCloud/publink for files when Scan Repo button clicked
            download_files_clicked(self)
                Calls download_files method when Download button clicked
            load_shot_table_data(self, results=[])
                Loads selected shot columns and rows in dt_shot_data Data Table
            load_filename_table(self, results=[], headers=[])
                Loads selected files/assets in dt_files Data Table
            add_publink_to_table(self)
                Adds user-inputted publink to dt_cloud_links Data Table
            get_codes(self)
                Returns PCloud API call response codes
            search_for_files(self)
                Searches pcloud publinks for selected files
            get_publink_data(self, codes=[])
                Returns publink metadata
            classify_files(self)
                Classifies files according to file extensions
            color_filename_cells(self)
                Colors cells of dt_files Data Table based on file status
            color_shot_table(self)
                Colors cells of dt_shot_data_table Data table based on file status
            get_matching_files(self, filename="")
                Returns list of filenames with multiple pcloud entries
            find_latest_file(self, file_data=[])
                Returns latest modified file from list of same-named filenames
            download_files(self)
                Downloads assets/files to respective directory. Disables download button for download length
            update_progress_bar(self, percent=0)
                Updates progress bar of main window to reflect download progress
            download_finished(self)
                Enables download button on download completion
            create_unique_filename_list(self, assets=[])
                Returns list of unique filename from list of filenames
            set_shot_data(self, data=[])
                Sets shot_data to user selections
            test_popup(self)
                Pops up FileDetailsView
    """
    def __init__(self, parent=None, file_io=FileIo()):
        """Constructor:
            Initialize Results Output View

            Parameters:
                self
                parent : QFrame
                file_io : FileIo
                    !!! File input & output
            Returns:
                None
        """
        # -------------------------------------------init Start-------------------------------------------
        super(GCResultsOutputView, self).__init__(parent)
        self.parent = parent
        self.shot_data = []
        self.filenames = []
        self.file_metadata = []
        self.publinks = []
        self.cloud_scanned = False
        self.fio = file_io
        self.apic = PCloud()
        self.apic.set_region("NA")

        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())
        # ----------------------------------------------
        # -----------------hbl_tables-------------------
        # ----------------------------------------------
        self.hbl_tables = QHBoxLayout()

        self.dt_shot_data = DataTable(None, readonly=False)
        self.dt_files = SimpleDataTable(None, readonly=True)

        self.btn_update = QPushButton("Update Filenames ---->")
        self.btn_update.clicked.connect(self.load_filename_table)

        self.hbl_tables.addWidget(self.dt_shot_data, stretch=4)
        self.hbl_tables.addWidget(self.btn_update)
        self.hbl_tables.addWidget(self.dt_files, stretch=1)

        # ----------------------------------------------
        # -----------------hbl_controls-----------------
        # ----------------------------------------------
        self.hbl_controls = QHBoxLayout()

        # Publink list
        self.dt_cloud_links = SimpleDataTable(None, readonly=True)
        self.dt_cloud_links.load_table([])
        self.dt_cloud_links.set_headers(["Publinks"])

        # Publink labeled input with button
        self.liwb_add_publink = LabeledInputWithButton(self, label_text="pCloud Publink: ", button_text="Add Link")
        self.liwb_add_publink.button.clicked.connect(self.add_publink_clicked)

        # vbl_control_buttons
        self.vbl_control_buttons = QVBoxLayout()

        # Scan button
        self.btn_scan = QPushButton(text="Scan Linked Repos")
        self.btn_scan.clicked.connect(self.scan_pcloud_clicked)

        # Download Button
        self.btn_download_files = QPushButton(text="Download Scanned Files")
        self.btn_download_files.clicked.connect(self.download_files)

        self.vbl_control_buttons.addWidget(self.liwb_add_publink)
        self.vbl_control_buttons.addWidget(self.btn_scan, alignment=Qt.AlignHCenter)
        self.vbl_control_buttons.addWidget(self.btn_download_files, alignment=Qt.AlignHCenter)

        self.hbl_controls.addWidget(self.dt_cloud_links)
        self.hbl_controls.addLayout(self.vbl_control_buttons)

        # -------------------------------------------------
        # -----------------vbl_main_layout-----------------
        # -------------------------------------------------
        self.vbl_main_layout = QVBoxLayout()

        self.vbl_main_layout.addLayout(self.hbl_tables, stretch=4)
        self.vbl_main_layout.addLayout(self.hbl_controls, stretch=1)
        self.vbl_main_layout.setContentsMargins(30, 20, 30, 30)

        self.setLayout(self.vbl_main_layout)
        self.setGeometry(0, 0, 900, 600)
        self.setStyleSheet('QFrame DataTable{border:1px solid #1000A0;background-color:#e6e6e6;}')

        # -------------------------------------------init End-------------------------------------------
    def add_publink_clicked(self):
        self.add_publink_to_table()

    def scan_pcloud_clicked(self):
        self.search_for_files()
        self.classify_files()
        self.color_filename_cells()
        self.color_shot_table()
        for file in self.file_metadata:
            print(file)

    def download_files_clicked(self):
        self.download_files()

    def load_shot_table_data(self, selected_shots=[]):
        try:
            headers = selected_shots.pop(0)
            self.dt_shot_data.load_table(selected_shots)
            self.dt_shot_data.set_headers(headers)

            self.load_filename_table()
        except IndexError or PermissionError:
            pass

    def load_filename_table(self):
        shot_headers = self.dt_shot_data.get_headers()
        shot_data = self.dt_shot_data.get_table_data()

        raw_filenames = []
        if "ShotCode" in shot_headers:
            index = shot_headers.index('ShotCode')
            for item in shot_data:
                raw_filenames.insert(-1, item[index])

        if "Assets" in shot_headers:
            index = shot_headers.index('Assets')
            for item in shot_data:
                raw_filenames.insert(-1, item[index])

        self.filenames = self.create_unique_filename_list(raw_filenames)

        self.filenames.sort()
        self.dt_files.set_dimensions(1, len(shot_data))
        header = ["Filenames"]
        self.dt_files.set_headers(header)
        self.dt_files.load_table(self.filenames)

    def add_publink_to_table(self):
        publink = self.liwb_add_publink.get_input_text()
        if publink and publink not in self.publinks:
            self.publinks.append(publink)
            self.dt_cloud_links.load_table(data=self.publinks)
            self.liwb_add_publink.set_input_text("")

    def get_codes(self):
        codes = []
        for publink in self.publinks:
            codes.append(self.apic.get_code_from_url(publink))
        return codes

    def search_for_files(self):
        if codes := self.get_codes():
            if publink_data := self.get_publink_data(codes):
                self.file_metadata = []
                for filename in self.filenames:
                    for i in range(len(publink_data)):
                        if found_files := self.apic.get_pub_link_file_data(filename, publink_data[i]):
                            if type(found_files) is list:
                                for file in found_files:
                                    file.publink_code = codes[i]
                                    self.file_metadata.append(file)
                            else:
                                file.publink_code = codes[i]
                                self.file_metadata.append(found_files)

    def get_publink_data(self, codes=[]):
        publink_data = []
        if codes:
            for code in codes:
                data = self.apic.get_pub_link_directory(code)["metadata"]
                publink_data.append(data)
            return publink_data
        else:
            return None

    def classify_files(self):
        file_extensions = {
            "audio": ["wav", "mp3", "ogg", "flac"],
            "video": ["mov", "mp4", "mpg", "avi", "wmv"],
            "image": ["jpg", "gif", "bmp", "fla", "psd", "png"]
        }

        for i in range(len(self.file_metadata)):
            file_data = self.file_metadata[i]
            file_extension = file_data.name[-4:]
            for file_type in file_extensions:
                if not self.file_metadata[i].file_type:
                    for extension in file_extensions[file_type]:
                        if extension in file_extension:
                            self.file_metadata[i].file_type = str(file_type)

    def color_filename_cells(self):
        for i in range(len(self.filenames)):
            filename = self.filenames[i]
            matched_files = self.get_matching_files(filename)
            number_of_matches = len(matched_files)

            if number_of_matches == 0:
                self.dt_files.set_cell_color(0, i, color="red")
                self.dt_files.set_text_color(0, i, "white")
                self.dt_files.set_cell_tooltip(0, i, "File not found!")
            elif number_of_matches > 1:
                self.dt_files.set_cell_color(0, i, color="yellow")
                self.dt_files.set_text_color(0, i, "black")
                self.dt_files.set_cell_tooltip(0, i, "Multiple files found!")
            elif number_of_matches == 1:
                self.dt_files.set_cell_color(0, i, color="green")
                self.dt_files.set_text_color(0, i, "black")
                self.dt_files.set_cell_tooltip(0, i, "Exact Match found!")

    def color_shot_table(self):
        for i in range(len(self.filenames)):
            filename = self.filenames[i]
            matched_files = self.get_matching_files(filename)
            number_of_matches = len(matched_files)

            dimensions = self.dt_shot_data.get_dimensions()

            for y in range(dimensions["y"]):
                for x in range(dimensions["x"]):
                    cell_text = self.dt_shot_data.get_cell_text(x, y)
                    if "," in cell_text:
                        cell_text = cell_text.split(",")
                    else:
                        cell_text = [cell_text]

                    if filename in cell_text:
                        if number_of_matches == 0:
                            self.dt_shot_data.set_cell_color(x, y, color="red")
                            self.dt_shot_data.set_text_color(x, y, "white")
                            self.dt_shot_data.set_cell_tooltip(x, y, "File not found!")
                        elif number_of_matches > 1:
                            self.dt_shot_data.set_cell_color(x, y, color="yellow")
                            self.dt_shot_data.set_text_color(x, y, "black")
                            self.dt_shot_data.set_cell_tooltip(x, y, "Multiple files found!")
                        elif number_of_matches == 1:
                            self.dt_shot_data.set_cell_color(x, y, color="green")
                            self.dt_shot_data.set_text_color(x, y, "black")
                            self.dt_shot_data.set_cell_tooltip(x, y, "Exact Match found!")

    def get_matching_files(self, filename=""):
        matched_files = []
        for file_data in self.file_metadata:
            if filename in file_data.name:
                matched_files.append(file_data)
        return matched_files

    def find_latest_file(self, file_data=[]):
        latest_file = {}
        latest_date = 0
        for item in file_data:
            if item.name[-3:] == "fla" or item.name[-3:] == "psd" or item.name[-3:] == "wav" or item.name[-3:] == "mov":
                modified_date = item.modified
                modified_date = datetime.strptime(modified_date, '%a, %d %b %Y %H:%M:%S %z')
                unix_timestamp = modified_date.timestamp()
                if unix_timestamp > latest_date:
                    latest_date = unix_timestamp
                    latest_file = item
        return latest_file

    def download_files(self):
        self.btn_download_files.setEnabled(False)
        print("Download Button Pressed")
        worker = DownloadWorker(self.file_metadata, self.fio)
        worker.signals.update_progress.connect(self.update_progress_bar)
        worker.signals.finished.connect(self.download_finished)
        self.threadpool.start(worker)

    @Slot()
    def update_progress_bar(self, percent=0):
        main_window = self.parent.parent
        main_window.progress_bar.setValue(percent)

    @Slot()
    def download_finished(self):
        self.btn_download_files.setEnabled(True)

    def create_unique_filename_list(self, assets=[]):
        asset_set = set()
        for item in assets:
            if "," in item:
                sub_list = [x.strip() for x in item.split(',')]
                asset_set = asset_set.union(set(sub_list))
            else:
                asset_set.add(item)
        return list(asset_set)

    def set_shot_data(self, data=[]):
        self.shot_data = data

    def test_popup(self):
        popup_frame = FileDetailsView()
        popup_frame.show()
        popup_frame.exec_()


if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    resOut = GCResultsOutputView()
    resOut.show()
    sys.exit(qApp.exec_())
