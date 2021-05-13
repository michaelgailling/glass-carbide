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
import sys
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QComboBox, QFrame, QVBoxLayout, QLabel, QGridLayout, QHBoxLayout

from GC_Components.InputComponents import LabeledDirectoryInput, LabeledInput, LabeledInputWithButton
from GC_Components.TableComponents import DataTable, AssetDataTable
from GC_Services.FileIo import FileIo
from GC_Services.pcloudAPI import PCloud


class ResultsOutputView(QFrame):
    def __init__(self, parent=None, file_io=FileIo()):
        # -------------------------------------------init Start-------------------------------------------
        super(ResultsOutputView, self).__init__(parent)

        self.data = []
        self.assets = []
        self.fio = file_io

        # ----------------------------------------------
        # -----------------hbl_tables-------------------
        # ----------------------------------------------
        self.hbl_tables = QHBoxLayout()

        self.dt_data = DataTable(self, readonly=True)
        self.dt_assets = AssetDataTable(self, readonly=True)

        self.hbl_tables.addWidget(self.dt_data, stretch=4)
        self.hbl_tables.addWidget(self.dt_assets, stretch=1)

        # ----------------------------------------------
        # -----------------vbl_controls-----------------
        # ----------------------------------------------
        self.vbl_controls = QVBoxLayout()
        self.vbl_controls.setSpacing(1)

        # Root Directory Mapping input
        self.liwb_publink = LabeledInputWithButton(self, label_text="pCloud Publink: ", button_text="Scan Public Repo")
        self.liwb_publink.button.clicked.connect(self.check_pcloud)

        self.vbl_controls.addWidget(self.liwb_publink)

        # -------------------------------------------------
        # -----------------vbl_main_layout-----------------
        # -------------------------------------------------
        self.vbl_main_layout = QVBoxLayout()

        self.vbl_main_layout.addItem(self.hbl_tables)
        self.vbl_main_layout.addItem(self.vbl_controls)
        self.vbl_main_layout.setContentsMargins(30, 20, 30, 30)

        self.setLayout(self.vbl_main_layout)
        self.setGeometry(0, 0, 900, 600)
        self.setStyleSheet('QFrame DataTable{border:1px solid #1000A0;background-color:#e6e6e6;}'
                           'LabeledInputWithButton QLabel{font-weight:600}')

        # -------------------------------------------init End-------------------------------------------

    def check_pcloud(self):
        publink = self.liwb_publink.get_input_text()
        if publink:
            apic = PCloud()
            apic.set_region("NA")
            code = apic.get_code_from_url(publink)
            publink_data = apic.get_pub_link_directory(code)

            for i in range(0, len(self.assets)):
                file_data = apic.get_pub_link_file_data(self.assets[i], publink_data["metadata"])
                print(file_data)
                if not file_data:
                    self.dt_assets.set_cell_color(0, i, color="red")
                    self.dt_assets.set_text_color(0, i, "white")
                    self.dt_assets.set_cell_tooltip(0, i, "File not found!")
                elif len(file_data) > 1:
                    self.dt_assets.set_cell_color(0, i, color="yellow")
                    self.dt_assets.set_text_color(0, i, "black")
                    self.dt_assets.set_cell_tooltip(0, i, "Multiple files found! Most Recent Version Used!")
                else:
                    self.dt_assets.set_cell_color(0, i, color="green")
                    self.dt_assets.set_text_color(0, i, "black")
                    self.dt_assets.set_cell_tooltip(0, i, "Exact Match found!")

    def asset_cell_clicked(self):
        pass

    def load_table_data(self, results=[]):
        try:
            headers = results.pop(0)
            self.dt_data.load_table(results)
            self.dt_data.set_headers(headers)

            self.load_asset_data(results, headers)
        except IndexError or PermissionError:
            pass

    def load_asset_data(self, results=[], headers=[]):
        ind = headers.index('Assets')
        assets = []
        for result in results:
            assets.insert(-1, result[ind])

        asset_set = set()
        for item in assets:
            if "," in item:
                sub_list = [x.strip() for x in item.split(',')]
                asset_set = asset_set.union(set(sub_list))

        self.assets = list(asset_set)
        self.assets.sort()
        self.dt_assets.set_dimensions(1, len(results))
        header = [headers.pop(ind)]
        self.dt_assets.set_headers(header)
        self.dt_assets.load_table(self.assets)

    def set_data(self, data=[]):
        self.data = data


if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    resOut = ResultsOutputView()
    resOut.show()
    sys.exit(qApp.exec_())
