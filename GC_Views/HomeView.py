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
        self.newBtn.setStyleSheet("background-color:rgb(85,0,255); color:rgb(255,255,255);")
        self.openBtn = QPushButton("Open")
        self.openBtn.setStyleSheet("background-color:rgb(85,0,255); color:rgb(255,255,255);")
        self.saveBtn = QPushButton("Save")
        self.saveBtn.setStyleSheet("background-color:rgb(85,0,255); color:rgb(255,255,255);")
        self.exitBtn = QPushButton("Exit")
        self.exitBtn.setStyleSheet("color:rgb(85,0,255); background-color:rgb(255,255,255);\n"
                                   " border: 2px solid rgb(85,0,255);")
        # Add buttons to Vbox widget
        self.btnBox.addWidget(self.newBtn)
        self.btnBox.addWidget(self.openBtn)
        self.btnBox.addWidget(self.saveBtn)
        self.btnBox.addWidget(self.exitBtn)
        # Logo Picture will be contained in a Label
        self.logo = QLabel("Logo Placeholder")
        self.imgBox.addWidget(self.logo, alignment=Qt.AlignHCenter)
        # Layout loading
        self.layout.addItem(self.btnBox)
        self.layout.addItem(self.imgBox)
        self.setLayout(self.layout)
        self.setGeometry(0, 0, 800, 400)


if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    hom = HomeView()
    hom.show()
    sys.exit(qApp.exec_())



