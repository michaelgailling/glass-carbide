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
from ExistingDirectoryView import ExistingDirectoryView
from HomeBtnsView import HomeBtnsView
from pCloudView import PCloudView
from LogoView import LogoView


class HomeView(QFrame):
    """Home View

                    Summary:
                        A class for {Type} that includes:

                        -{Description} to the {Location eg left}

                    Attributes:
                        label, {AttributeName}

                    Methods:
                        get_input_text, {MethodName}

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
        super(HomeView, self).__init__(parent)

        # -------------------------------------
        # -----------------fio-----------------
        # -------------------------------------
        self.fio = file_io

        # -------------------------------------------------
        # -----------------vbl_left_layout-----------------
        # -------------------------------------------------

        self.vbl_left_layout = QVBoxLayout()

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
        self.hbv_home_buttons.openBtn.clicked.connect(lambda: self.set_frame_index(2))

        # --------------------------------------------------
        # -----------------vbl_right_layout-----------------
        # --------------------------------------------------

        self.vbl_right_layout = QVBoxLayout()

        # Initialize vbl_right_layout GUI Elements
        self.sw_project_setup = QStackedWidget(parent=self)

        # Initialize Directory Mapping Views
        self.frm_blank = QFrame(parent=self)
        self.dmv_mapping_view = DirectoryMappingView(parent=self, file_io=self.fio)
        self.edv_existing_view = ExistingDirectoryView(parent=self)

        # Add views to sw_project_setup
        self.sw_project_setup.addWidget(self.frm_blank)
        self.sw_project_setup.addWidget(self.dmv_mapping_view)
        self.sw_project_setup.addWidget(self.edv_existing_view)

        # Store the current Index for external use
        self.current_frame_index = 0

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

        self.setStyleSheet('HomeBtnsView{border:none} LogoView{border:none} QLabel{border:none}')

        # -------------------------------------------init End-------------------------------------------

    def set_frame_index(self, num=0):
        self.current_frame_index = num
        self.sw_project_setup.setCurrentIndex(num)


if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    hom = HomeView()
    hom.show()
    sys.exit(qApp.exec_())



