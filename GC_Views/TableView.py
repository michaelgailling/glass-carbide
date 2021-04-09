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


class TableView(QFrame):
    def __init__(self, parent=None):
        super(TableView, self).__init__(parent)
        self.layout = QVBoxLayout()
        self.hbox = QHBoxLayout()
        # Table
        self.table = QTableWidget()
        self.setStyleSheet("margin: 0% 3% 25% 3%;")
        # Button
        self.loadBtn = QPushButton("Load CSV")
        self.loadBtn.setStyleSheet("background-color:rgb(85,0,255); color:rgb(255,255,255);")
        self.hbox.addWidget(self.loadBtn)
        # Label
        self.displayLbl = QLabel("CSV TYPE/PURPOSE LABEL")
        self.displayLbl.setStyleSheet("color: rgb(85, 0, 255);")
        self.hbox.addWidget(self.displayLbl, alignment=Qt.AlignRight)
        # Layout loading
        self.layout.addWidget(self.table)
        self.layout.addItem(self.hbox)
        self.setLayout(self.layout)
        self.setGeometry(0, 0, 800, 500)


"""
if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    tab = TableView()
    tab.show()
    sys.exit(qApp.exec_())
"""
