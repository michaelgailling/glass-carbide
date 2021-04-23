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
from PySide2.QtWidgets import QApplication, QFrame, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QStackedWidget
from DirectoryMappingView import DirectoryMappingView
from ServerSelectionView import ServerSelectionView


class HomeBtnsView(QFrame):
    def __init__(self, parent=None):
        super(HomeBtnsView, self).__init__(parent)
        self.layout = QHBoxLayout()
        self.btnBox = QVBoxLayout()

        # Buttons
        self.newBtn = QPushButton("New")
        self.newBtn.setStyleSheet("background-color:rgb(85,0,255); color:rgb(255,255,255);margin:1 80; padding:2 20")
        self.openBtn = QPushButton("Open")
        self.openBtn.setStyleSheet("background-color:rgb(85,0,255); color:rgb(255,255,255);margin:1 80; padding:2 20")
        self.saveBtn = QPushButton("Save")
        self.saveBtn.setStyleSheet("background-color:rgb(85,0,255); color:rgb(255,255,255);margin:1 80; padding:2 20")
        self.mysteryBtn = QPushButton("???")
        self.mysteryBtn.setStyleSheet("background-color:rgb(85,0,255); color:rgb(255,255,255);margin:1 80; padding:2 20")
        self.exitBtn = QPushButton("Exit")
        self.exitBtn.setStyleSheet("color:rgb(85,0,255); background-color:rgb(255,255,255);\n"
                                   " border:2px solid rgb(85,0,255);margin:1 80; padding:2 20")
        self.exitBtn.clicked.connect(lambda: self.topLevelWidget().close())

        self.btnBox.addWidget(self.newBtn)
        self.btnBox.addWidget(self.openBtn)
        self.btnBox.addWidget(self.saveBtn)
        self.btnBox.addWidget(self.mysteryBtn)
        self.btnBox.addWidget(self.exitBtn)

        self.layout.addItem(self.btnBox)
        self.setLayout(self.btnBox)


if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    hom = HomeBtnsView()
    hom.show()
    sys.exit(qApp.exec_())

