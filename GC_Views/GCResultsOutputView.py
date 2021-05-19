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
from datetime import datetime
import sys

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QFrame, QVBoxLayout, QHBoxLayout, QPushButton

from GC_Components.InputComponents import LabeledInputWithButton
from GC_Components.TableComponents import DataTable, SimpleDataTable
from GC_Services.FileIo import FileIo
from GC_Services.pcloudAPI import PCloud


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
            data : []
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

        self.data = []
        self.filenames = []
        self.file_metadata = []
        self.publinks = []
        self.cloud_scanned = False
        self.fio = file_io

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
        self.btn_download.clicked.connect(self.download_assets)
        self.btn_download.setEnabled(False)

        self.vbl_control_buttons.addWidget(self.liwb_publink)
        self.vbl_control_buttons.addWidget(self.btn_scan)
        self.vbl_control_buttons.addWidget(self.btn_download)

        self.hbl_controls.addWidget(self.dt_cloud_links)
        self.hbl_controls.addLayout(self.vbl_control_buttons)

        # -------------------------------------------------
        # -----------------vbl_main_layout-----------------
        # -------------------------------------------------
        self.vbl_main_layout = QVBoxLayout()

        self.vbl_main_layout.addLayout(self.hbl_tables, stretch=4)
        self.vbl_main_layout.addLayout(self.hbl_controls, stretch=2)
        self.vbl_main_layout.setContentsMargins(30, 20, 30, 30)

        self.setLayout(self.vbl_main_layout)
        self.setGeometry(0, 0, 900, 600)
        self.setStyleSheet('QFrame DataTable{border:1px solid #1000A0;background-color:#e6e6e6;}')

        # -------------------------------------------init End-------------------------------------------

    def add_cloud_link(self):
        publink = self.liwb_publink.get_input_text()
        if publink not in self.publinks:
            self.publinks.append(publink)
            self.dt_cloud_links.load_table(data=self.publinks)

    def check_pcloud(self):
        apic = PCloud()
        apic.set_region("NA")

        publink_cumulative_data = {}

        if self.publinks:
            for publink in self.publinks:
                code = apic.get_code_from_url(publink)
                publink_data = apic.get_pub_link_directory(code)["metadata"]
                if not publink_cumulative_data:
                    publink_cumulative_data = publink_data
                else:
                    publink_cumulative_data["contents"].extend(publink_data["contents"])

            for i in range(0, len(self.filenames)):
                file_data = apic.get_pub_link_file_data(self.filenames[i], publink_cumulative_data)

                if not file_data:
                    self.dt_files.set_cell_color(0, i, color="red")
                    self.dt_files.set_text_color(0, i, "white")
                    self.dt_files.set_cell_tooltip(0, i, "File not found!")
                elif len(file_data) > 1:
                    self.dt_files.set_cell_color(0, i, color="yellow")
                    self.dt_files.set_text_color(0, i, "black")
                    self.dt_files.set_cell_tooltip(0, i, "Multiple files found! Most Recent Version Used!")
                    latest_file = self.find_latest_file(file_data=file_data)
                    if latest_file:
                        self.file_metadata.append(latest_file)
                else:
                    self.dt_files.set_cell_color(0, i, color="green")
                    self.dt_files.set_text_color(0, i, "black")
                    self.dt_files.set_cell_tooltip(0, i, "Exact Match found!")
                    self.file_metadata.extend(file_data)

            for item in self.file_metadata:
                print(item)
            self.cloud_scanned = True

    def find_latest_file(self, file_data=[]):
        latest_file = {}
        latest_date = 0
        for item in file_data:
            if item.name[-3:] == "fla" or item.name[-3:] == "psd":
                modified_date = item.modified
                modified_date = datetime.strptime(modified_date, '%a, %d %b %Y %H:%M:%S %z')
                unix_timestamp = modified_date.timestamp()
                if unix_timestamp > latest_date:
                    latest_date = unix_timestamp
                    latest_file = item
        return latest_file

    def download_assets(self):
        pass

    def asset_cell_clicked(self):
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
        index = shot_headers.index('ShotCode')
        for item in shot_data:
            raw_filenames.insert(-1, item[index])

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

    def set_data(self, data=[]):
        self.data = data


if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    resOut = GCResultsOutputView()
    resOut.show()
    sys.exit(qApp.exec_())
