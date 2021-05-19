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
from PySide2.QtGui import QFont
from PySide2.QtWidgets import QApplication, QFrame, QVBoxLayout, QHBoxLayout, QLabel, QStackedWidget, QPushButton
from GC_Services.FileIo import FileIo
from ExistingDirectoryView import ExistingDirectoryView
from GC_Views.GCCreateDirectoryView import GCCreateDirectoryView
from GC_Views.GCLogoView import GCLogoView


class GCHomeView(QFrame):
    """GC Home View

        Summary:
            A class for {Type} that includes:

            -{Description} to the {Location eg left}

        Attributes:


        Methods:


        Attributes
        ----------


        Methods
        -------

    """
    def __init__(self, parent=None, file_io=FileIo()):
        """Constructor:
            Initialize Home View

            Parameters:
                self
                parent : QFrame
                file_io : FileIo
                    !!! File input & output
            Returns:
                None
        """
        # -------------------------------------------init Start-------------------------------------------
        super(GCHomeView, self).__init__(parent)

        # -------------------------------------
        # -----------------fio-----------------
        # -------------------------------------
        self.fio = file_io

        # -------------------------------------------------
        # -----------------vbl_left_layout-----------------
        # -------------------------------------------------

        self.vbl_left_layout = QVBoxLayout()

        # Initialize vbl_left_layout GUI Elements
        # Instructions Label
        self.lbl_instructions = QLabel("Overview of Instructions")
        self.lbl_instructions.setAlignment(Qt.AlignCenter)
        font = QFont("Helvetica", 11, 300, True)
        self.lbl_instructions.setFont(font)
        self.lbl_instructions.setStyleSheet('QLabel{margin:auto auto 175 auto}')

        self.btn_start = QPushButton("Setup Project")
        # self.btn_open = QPushButton("Existing Directory")
        self.btn_exit = QPushButton("Exit")
        self.btn_exit.setStyleSheet("margin:75 auto 0 auto;color:#1000A0; background-color:rgb(255,255,255);padding:10;"
                                    "border:2px solid #1000A0;border-radius:20px")
        self.btn_start.setStyleSheet('margin-bottom:10')

        # Setup vbl_left_layout
        self.vbl_left_layout.addWidget(self.lbl_instructions)
        self.vbl_left_layout.addWidget(self.btn_start)
        # self.vbl_left_layout.addWidget(self.btn_open)
        self.vbl_left_layout.addWidget(self.btn_exit)
        self.vbl_left_layout.setAlignment(Qt.AlignCenter)

        # Assign methods for buttons
        self.btn_start.clicked.connect(self.set_new_project_frame)
        # self.btn_open.clicked.connect(self.set_existing_project_frame)
        self.btn_exit.clicked.connect(lambda: self.topLevelWidget().close())

        # --------------------------------------------------
        # -----------------vbl_right_layout-----------------
        # --------------------------------------------------

        self.vbl_right_layout = QVBoxLayout()

        # Initialize vbl_right_layout GUI Elements
        self.sw_project_setup = QStackedWidget()

        # Initialize Directory Mapping Views
        self.lv_logo = GCLogoView()
        self.cdv_create_view = GCCreateDirectoryView(None, file_io=self.fio)
        # self.edv_existing_view = ExistingDirectoryView(None)

        # Add views to sw_project_setup
        self.sw_project_setup.addWidget(self.lv_logo)
        self.sw_project_setup.addWidget(self.cdv_create_view)
        # self.sw_project_setup.addWidget(self.edv_existing_view)

        # Setup vbl_right_layout
        self.vbl_right_layout.addWidget(self.sw_project_setup)

        # -------------------------------------------------
        # -----------------hbl_main_layout-----------------
        # -------------------------------------------------

        self.hbl_main_layout = QHBoxLayout()

        # Add vbl_left_layout and vbl_right_layout to hbl_main_layout
        self.hbl_main_layout.addItem(self.vbl_left_layout)
        self.hbl_main_layout.addItem(self.vbl_right_layout)
        self.setLayout(self.hbl_main_layout)
        self.setStyleSheet('QStackedWidget{border:3px solid #1000A0; margin:25 40; padding:20}')

        # -------------------------------------------init End-------------------------------------------

    def set_frame_index(self, num=0):
        self.sw_project_setup.setCurrentIndex(num)

    def get_frame_index(self):
        return self.sw_project_setup.currentIndex()

    def set_new_project_frame(self):
        self.set_frame_index(1)

    def set_existing_project_frame(self):
        self.set_frame_index(2)


if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    hom = GCHomeView()
    hom.show()
    sys.exit(qApp.exec_())



