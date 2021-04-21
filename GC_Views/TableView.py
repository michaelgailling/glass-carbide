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
import sys
import csv
from PySide2 import QtCore
from PySide2.QtCore import Qt
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtWidgets import QApplication, QWidget, QTabWidget, QMainWindow, QAction, QFrame, QPlainTextEdit, \
    QPushButton, QVBoxLayout, QFileDialog, QTableWidget, QTableWidgetItem, QHBoxLayout, QLabel, QMessageBox
from requests import *

from GC_Components.InputComponents import LabeledFileInput
from GC_Components.TableComponents import DataTable
from GC_Services.csvIO import CsvIo


class TableView(QFrame):
    def __init__(self, parent=None):
        super(TableView, self).__init__(parent)
        self.vBox = QVBoxLayout()
        self.csv_handler = CsvIo()

        # Table
        self.dt_table = DataTable(self, 5, 5)

        # Labeled File Input
        self.lfi_file_select = LabeledFileInput(self, label_text="Select CSV", file_type="CSV Format (*.csv)")

        # Load Button
        self.btn_load_file = QPushButton("Load File")
        self.btn_load_file.clicked.connect(self.load_file)

        # Layout loading
        self.vBox.addWidget(self.dt_table)
        self.vBox.addWidget(self.lfi_file_select)
        self.vBox.addWidget(self.btn_load_file)
        self.setLayout(self.vBox)
 
        self.setGeometry(0, 0, 800, 500)

    def load_file(self):
        input_path = self.lfi_file_select.get_input_text()

        if input_path:
            self.csv_handler.import_data(input_path)

            csv_headers = self.csv_handler.data[0]
            csv_data = self.csv_handler.data[1:]

            width = len(csv_data[0])
            height = len(csv_data)

            self.dt_table.set_dimensions(width, height)
            self.dt_table.table.setHorizontalHeaderLabels(csv_headers)

            for y in range(len(csv_data)):
                for x in range(len(csv_data[y])):
                    cell = QTableWidgetItem(csv_data[y][x])
                    self.dt_table.table.setItem(y, x, cell)


if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    tab = TableView()
    tab.show()
    sys.exit(qApp.exec_())

