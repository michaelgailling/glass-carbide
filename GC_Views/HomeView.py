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


class HomeView(QFrame):
    def __init__(self, parent=None):
        super(HomeView, self).__init__(parent)
        self.layout = QHBoxLayout()
        self.btnBox = QVBoxLayout()
        self.frameBox = QVBoxLayout()

        # Step Instructions
        self.instruct = QLabel("Overview of Instructions")

        # Buttons
        self.newBtn = QPushButton("New")
        self.newBtn.setStyleSheet("background-color:rgb(85,0,255); color:rgb(255,255,255);margin:1 80; padding:2 20")
        self.newBtn.clicked.connect(lambda: self.set_frame_index(1))
        self.openBtn = QPushButton("Open")
        self.openBtn.setStyleSheet("background-color:rgb(85,0,255); color:rgb(255,255,255);margin:1 80; padding:2 20")
        self.openBtn.clicked.connect(lambda: self.set_frame_index(2))
        self.saveBtn = QPushButton("Save")
        self.saveBtn.setStyleSheet("background-color:rgb(85,0,255); color:rgb(255,255,255);margin:1 80; padding:2 20")
        self.saveBtn.clicked.connect(lambda: self.set_frame_index(2))
        self.mysteryBtn = QPushButton("???")
        self.mysteryBtn.setStyleSheet("background-color:rgb(85,0,255); color:rgb(255,255,255);margin:1 80; padding:2 20")
        self.mysteryBtn.clicked.connect(lambda: self.set_frame_index(0))
        self.exitBtn = QPushButton("Exit")
        self.exitBtn.setStyleSheet("color:rgb(85,0,255); background-color:rgb(255,255,255);\n"
                                   " border:2px solid rgb(85,0,255);margin:1 80; padding:2 20")
        self.exitBtn.clicked.connect(lambda: self.topLevelWidget().close())

        # Logo Picture will be contained in a Label
        self.logo = QLabel("Logo Placeholder")
        self.logo.setFixedHeight(100)
        self.btnBox.addWidget(self.logo, alignment=Qt.AlignHCenter)

        # Add buttons to Vbox widget
        self.btnBox.addWidget(self.instruct, alignment=Qt.AlignHCenter)
        self.btnBox.addWidget(self.newBtn)
        self.btnBox.addWidget(self.openBtn)
        self.btnBox.addWidget(self.saveBtn)
        self.btnBox.addWidget(self.mysteryBtn)
        self.btnBox.addWidget(self.exitBtn)
        self.btnBox.setSpacing(-15)

        # Stacked widget for mapping views
        self.resultFrame = QStackedWidget()
        self.resultFrame.setStyleSheet('QStackedWidget{border:2px solid blue;background-color:white;}')
        # Blank QFrame for initial load
        self.blank = QFrame()
        # Mapping view to map project folders
        self.mappingView = DirectoryMappingView()
        self.mappingView.setStyleSheet('QFrame{border:none;}')
        # Server selection view to pick local or server directory
        self.serverView = ServerSelectionView()
        # Load views to stacked widget
        self.resultFrame.addWidget(self.blank)
        self.resultFrame.addWidget(self.mappingView)
        self.resultFrame.addWidget(self.serverView)
        # Vbo
        self.frameBox.addWidget(self.resultFrame)

        # Layout loading
        self.layout.addItem(self.btnBox)
        self.layout.addWidget(self.resultFrame)
        self.setLayout(self.layout)
        self.setGeometry(0, 0, 800, 500)

    def set_frame_index(self, num: int):
        self.resultFrame.setCurrentIndex(num)

    def set_blank_frame(self):
        self.resultFrame.setCurrentIndex(0)


if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    hom = HomeView()
    hom.show()
    sys.exit(qApp.exec_())



