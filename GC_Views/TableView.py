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


class TableView(QFrame):
    def __init__(self, parent=None):
        super(TableView, self).__init__(parent)
        self.vBox = QVBoxLayout()
        # Table
        self.table = DataTable(self, 5, 5)
        # Labeled File Input
        self.file_select = LabeledFileInput(self, label_text="Select CSV", file_type="CSV Format (*.csv)")
        # Layout loading
        self.vBox.addWidget(self.table)
        self.vBox.addWidget(self.file_select)
        self.setLayout(self.vBox)
        self.setGeometry(0, 0, 800, 500)


if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    tab = TableView()
    tab.show()
    sys.exit(qApp.exec_())

