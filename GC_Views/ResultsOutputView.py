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

from GC_Components.InputComponents import LabeledDirectoryInput
from GC_Components.TableComponents import DataTable, AssetDataTable
from GC_Services.FileIo import FileIo


class ResultsOutputView(QFrame):
    def __init__(self, parent=None, file_io=FileIo()):
        super(ResultsOutputView, self).__init__(parent)
        self.layout = QVBoxLayout()
        self.grid = QGridLayout()
        self.data = []
        self.fio = file_io

        # Label
        self.displayLbl = QLabel("Review")

        # Root Directory Mapping input
        self.project_dir = LabeledDirectoryInput(self, label_text="Project Folder: ")

        # Combo Boxes
        self.softwareBox = QComboBox(self)
        self.softwareBox.addItem("Select Software   ...")
        self.softwareBox.setStyleSheet('::section{background-color:white;padding:10 10}')
        self.comboBox = QVBoxLayout()
        self.comboBox.setSpacing(1)

        # Results Display
        self.dt_data = DataTable()

        # Assets Display
        self.dt_assets = AssetDataTable(self)

        # HBox to contain results and assets tables
        self.tablesBox = QHBoxLayout()
        self.tablesBox.addWidget(self.dt_data, stretch=4)
        # self.tablesBox.addWidget(self.dt_data)
        self.tablesBox.addWidget(self.dt_assets, stretch=1)

        # Layout Loading
        self.comboBox.addWidget(self.project_dir)
        self.comboBox.addWidget(self.softwareBox, alignment=Qt.AlignHCenter)
        self.layout.addItem(self.tablesBox)
        self.layout.addItem(self.comboBox)
        self.layout.setContentsMargins(30, 20, 30, 30)
        self.setLayout(self.layout)

        self.setGeometry(0, 0, 900, 600)

    def load_table_data(self, results=[]):
        try:
            headers = results.pop(0)
            self.dt_data.load_data(results)
            self.dt_data.set_headers(headers)

            self.load_asset_data(results, headers)
        except IndexError or PermissionError:
            pass

    def load_asset_data(self, results=[], headers=[]):
        ind = headers.index('Assets')
        assets = []
        true_assets = {""}
        temp = []
        for result in results:
            assets.insert(-1, result[ind])

        asset_set = set()
        for item in assets:
            if "," in item:
                sub_list = [x.strip() for x in item.split(',')]
                asset_set = asset_set.union(set(sub_list))

        assets = list(asset_set)
        assets.sort()

        self.dt_assets.set_dimensions(1, len(results))
        header = [headers.pop(ind)]
        self.dt_assets.set_headers(header)
        self.dt_assets.load_data(assets)
        self.dt_assets.insert_data_column(header="Cloud Location", insert_before=False, data=[])

    def set_data(self, data=[]):
        self.data = data


if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    resOut = ResultsOutputView()
    resOut.show()
    sys.exit(qApp.exec_())
