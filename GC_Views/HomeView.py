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
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QApplication, QFrame, QVBoxLayout, QHBoxLayout, QLabel, QStackedWidget, QMessageBox
from DirectoryMappingView import DirectoryMappingView
from GC_Services.FileIo import FileIo
from ServerSelectionView import ServerSelectionView
from HomeBtnsView import HomeBtnsView
from pCloudView import  PCloudView
from LogoView import LogoView


class HomeView(QFrame):
    def __init__(self, parent=None, file_io=FileIo()):
        super(HomeView, self).__init__(parent)
        self.layout = QHBoxLayout()
        self.btnBox = QVBoxLayout()
        self.frameBox = QVBoxLayout()
        self.fio = file_io

        # Creation confirmation variable
        self.continue_create = True

        # Step Instructions
        self.instruct = QLabel("Overview of Instructions")

        # Home Buttons View with New, Open, Save & Exit buttons
        self.btnFrame = HomeBtnsView()

        # Assign methods for buttons
        self.btnFrame.newBtn.clicked.connect(lambda: self.set_frame_index(1))
        self.btnFrame.openBtn.clicked.connect(lambda: self.set_frame_index(3))
        self.btnFrame.saveBtn.clicked.connect(lambda: self.set_frame_index(2))

        # Logo Picture will be contained in a Label
        self.logo = LogoView()

        # Add logo, instructions and buttons frame
        self.btnBox.addWidget(self.logo, alignment=Qt.AlignHCenter)
        self.btnBox.addWidget(self.instruct, alignment=Qt.AlignHCenter)
        self.btnBox.addWidget(self.btnFrame)

        # Stacked widget for mapping views
        self.resultFrame = QStackedWidget()
        self.resultFrame.setStyleSheet('QStackedWidget{border:2px solid blue;background-color:white;}')
        # Blank QFrame for initial load
        self.blank = QFrame()
        # PCloud browser
        self.pCloudView = PCloudView()
        # Mapping view to map project folders
        self.mappingView = DirectoryMappingView(self, self.fio)
        self.mappingView.setStyleSheet('QFrame{border:none;}')
        # Server selection view to pick local or server directory
        self.serverView = ServerSelectionView()
        # Load views to stacked widget
        self.resultFrame.addWidget(self.blank)
        self.resultFrame.addWidget(self.mappingView)
        self.resultFrame.addWidget(self.serverView)
        self.resultFrame.addWidget(self.pCloudView)
        # Vbo
        self.frameBox.addWidget(self.resultFrame)

        # Layout loading
        self.layout.addItem(self.btnBox)
        self.layout.addWidget(self.resultFrame)
        self.setLayout(self.layout)
        self.setGeometry(0, 0, 800, 500)

    def set_frame_index(self, num: int):
        if self.resultFrame.currentIndex() == 0:
            self.confirm_create()
        if self.continue_create == True:
            self.resultFrame.setCurrentIndex(num)

    def confirm_create(self):
        self.continue_create = False
        msg = QMessageBox()
        msg.setWindowTitle("Are You Sure?")
        msg.setText("This will create new folders within the selected directories. Would you like to continue?")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.buttonClicked.connect(self.msg_button_click)

        returnValue = msg.exec()
        if returnValue == QMessageBox.Ok:
            print('OK clicked')
            self.continue_create = True
        elif returnValue == QMessageBox.Cancel:
            self.continue_create = False
        # msg.exec_()

    def msg_button_click(self):
        print("Button clicked")


if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    hom = HomeView()
    hom.show()
    sys.exit(qApp.exec_())



