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
from PySide2 import QtCore
from PySide2.QtCore import Qt
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtWidgets import QApplication, QWidget, QTabWidget, QMainWindow, QAction, QFrame, \
    QPushButton, QVBoxLayout, QFileDialog, QTableWidget, QTableWidgetItem, QHBoxLayout, QLabel
from TableView import TableView


class HomeView(QFrame):
    def __init__(self, parent=None):
        super(HomeView, self).__init__(parent)
        self.layout = QHBoxLayout()
        self.btnBox = QVBoxLayout()
        self.imgBox = QVBoxLayout()

        # Buttons
        self.newBtn = QPushButton("New")
        self.openBtn = QPushButton("Open")
        self.SaveBtn = QPushButton("Save")
        self.ExitBtn = QPushButton("Exit")

