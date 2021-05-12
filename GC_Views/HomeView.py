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
from pCloudView import PCloudView
from LogoView import LogoView


class HomeView(QFrame):
    def __init__(self, parent=None, file_io=FileIo()):
        super(HomeView, self).__init__(parent)

        # Store Reference to Global Object
        self.fio = file_io

        # Initialize Layouts
        self.hbl_main_layout = QHBoxLayout()
        self.vbl_left_layout = QVBoxLayout()
        self.vbl_right_layout = QVBoxLayout()

        # -----------------vbl_left_layout-----------------
        # Initialize vbl_left_layout GUI Elements
        self.lv_logo = LogoView(parent=self)
        self.lbl_instructions = QLabel("Overview of Instructions")
        self.hbv_home_buttons = HomeBtnsView(parent=self)

        # Setup vbl_left_layout
        self.vbl_left_layout.addWidget(self.lv_logo, alignment=Qt.AlignHCenter)
        self.vbl_left_layout.addWidget(self.lbl_instructions, alignment=Qt.AlignHCenter)
        self.vbl_left_layout.addWidget(self.hbv_home_buttons)

        # Assign methods for buttons
        self.hbv_home_buttons.startBtn.clicked.connect(lambda: self.set_frame_index(1))

        # -----------------vbl_right_layout-----------------
        # Initialize vbl_right_layout GUI Elements
        self.sw_project_setup = QStackedWidget(parent=self)

        # Initialize Directory Mapping Views
        self.frm_blank = QFrame(parent=self)
        self.dmv_mapping_view = DirectoryMappingView(parent=self, file_io=self.fio)

        # Add views to sw_project_setup
        self.sw_project_setup.addWidget(self.frm_blank)
        self.sw_project_setup.addWidget(self.dmv_mapping_view)

        # Setup vbl_right_layout
        self.vbl_right_layout.addWidget(self.sw_project_setup)

        # -----------------hbl_main_layout-----------------
        # Add vbl_left_layout and vbl_right_layout to hbl_main_layout
        self.hbl_main_layout.addItem(self.vbl_left_layout)
        self.hbl_main_layout.addItem(self.vbl_right_layout)
        self.setLayout(self.hbl_main_layout)

        self.setStyleSheet('HomeBtnsView{border:none} LogoView{border:none} QLabel{border:none}')

    def set_frame_index(self, num: int):
        self.sw_project_setup.setCurrentIndex(num)

if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    hom = HomeView()
    hom.show()
    sys.exit(qApp.exec_())



