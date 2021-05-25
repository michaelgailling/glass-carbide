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
import json
from datetime import datetime
import sys

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QFrame, QVBoxLayout, QHBoxLayout, QPushButton

from GC_Components.InputComponents import LabeledInputWithButton
from GC_Components.TableComponents import DataTable, SimpleDataTable
from GC_Services.FileIo import FileIo
from GC_Services.pcloudAPI import PCloud
from GCFileDetailsView import FileDetailsView


class GCResultsOutputView(QFrame):
    """Results Output View

        Summary:
            A class for {Type} that includes:

            -{Description} to the {Location eg left}

        Attributes:
            data, assets, file_metadata, cloud_scanned, fio, hbl_tables, vbl_controls, vbl_main_layout,
            dt_data, dt_assets, liwb_publink, btn_download

        Methods:
            check_pcloud, find_latest_file, download_assets, asset_cell_clicked, load_table_data,
            load_asset_data, set_data

        Attributes
        ----------
            shot_data : []
                Array for selected data from table view
            files : []
                Array of selected asset listings
            file_metadata : []
                !!! for !!!
            cloud_scanned : bool
                Bool for whether pCloud scan successful
            fio : FileIo
                !!! File input & output
            hbl_tables : QHBoxLayout
                HBox layout for tables
            hbl_controls : QVBoxLayout
                VBox layout for pCloud buttons
            vbl_main_layout = QVBoxLayout
                Main VBox layout
            dt_shot_data : DataTable
                Data Table for selected columns and rows
            dt_files : SimpleDataTable
                Data Table for selected assets
            liwb_publink = LabeledInputWithButton
                Labeled Input With Button for pCloud/publink access
            btn_download = QPushButton
                Button to download selected assets

        Methods
        -------
            check_pcloud(self)
                Checks pCloud/publink for assets
            find_latest_file(self, file_data=[])
                Returns latest modified file from list of same-named assets
            download_assets(self)
                Downloads assets to respective directory
            asset_cell_clicked(self)
                !!! when asset cell is clicked
            load_table_data(self, results=[])
                Loads selected columns and rows in Data Table
            load_asset_data(self, results=[], headers=[])
                Loads selected assets in Data Table
            set_data(self, data=[])
                !!! Sets data to !!!
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

        self.shot_data = []
        self.filenames = []
        self.file_metadata = []
        self.publinks = []
        self.cloud_scanned = False
        self.fio = file_io
        self.apic = PCloud()
        self.apic.set_region("NA")
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
        self.liwb_publink = LabeledInputWithButton(self, label_text="pCloud Publink: ", button_text="Add Link")
        self.liwb_publink.button.clicked.connect(self.add_cloud_link)

        # vbl_control_buttons
        self.vbl_control_buttons = QVBoxLayout()

        # Scan button
        self.btn_scan = QPushButton(text="Scan Linked Repos")
        self.btn_scan.clicked.connect(self.check_pcloud)

        # Download Button
        self.btn_download = QPushButton(text="Download Scanned Files")
        # self.btn_download.clicked.connect(self.download_assets)
        # self.btn_download.setEnabled(False)
        self.btn_download.clicked.connect(self.test_popup)

        self.vbl_control_buttons.addWidget(self.liwb_publink)
        self.vbl_control_buttons.addWidget(self.btn_scan, alignment=Qt.AlignHCenter)
        self.vbl_control_buttons.addWidget(self.btn_download, alignment=Qt.AlignHCenter)

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

    def add_cloud_link(self):
        publink = self.liwb_publink.get_input_text()
        if publink and publink not in self.publinks:
            self.publinks.append(publink)
            self.dt_cloud_links.load_table(data=self.publinks)
            self.liwb_publink.set_input_text("")

    def get_codes(self):
        codes = []
        for publink in self.publinks:
            codes.append(self.apic.get_code_from_url(publink))
        return codes

    def get_publink_data(self, codes=[]):
        publink_data = []
        if codes:
            for code in codes:
                data = self.apic.get_pub_link_directory(code)["metadata"]
                publink_data.append(data)
            return publink_data
        else:
            return None

    def check_pcloud(self):
        self.search_for_files()
        self.color_cells()

    def search_for_files(self):
        if codes := self.get_codes():
            if publink_data:= self.get_publink_data(codes):
                self.file_metadata = []
                for filename in self.filenames:
                    for i in range(len(publink_data)):
                        found_files = self.apic.get_pub_link_file_data(filename, publink_data[i])
                        if found_files:
                            if type(found_files) is list:
                                for file in found_files:
                                    file.publink_code = codes[i]
                                    self.file_metadata.append(file)
                            else:
                                file.publink_code = codes[i]
                                self.file_metadata.append(found_files)

                for file in self.file_metadata:
                    print(file)

    def color_cells(self):
        for i in range(len(self.filenames)):
            filename = self.filenames[i]
            matched_files = []
            for file_data in self.file_metadata:
                if filename in file_data.name:
                    matched_files.append(file_data)

            number_of_matches = len(matched_files)

            if number_of_matches == 0:
                self.dt_files.set_cell_color(0, i, color="red")
                self.dt_files.set_text_color(0, i, "white")
                self.dt_files.set_cell_tooltip(0, i, "File not found!")
            elif number_of_matches == 1:
                self.dt_files.set_cell_color(0, i, color="yellow")
                self.dt_files.set_text_color(0, i, "black")
                self.dt_files.set_cell_tooltip(0, i, "Multiple files found! Most Recent Version Used!")
            elif number_of_matches > 1:
                self.dt_files.set_cell_color(0, i, color="green")
                self.dt_files.set_text_color(0, i, "black")
                self.dt_files.set_cell_tooltip(0, i, "Exact Match found!")

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

    def download_assets(self):
        pass

    def filename_cell_clicked(self):
        pass

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

        self.filenames = self.create_unique_file_list(raw_filenames)

        self.filenames.sort()
        self.dt_files.set_dimensions(1, len(shot_data))
        header = ["Filenames"]
        self.dt_files.set_headers(header)
        self.dt_files.load_table(self.filenames)

    def create_unique_file_list(self, assets=[]):
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
