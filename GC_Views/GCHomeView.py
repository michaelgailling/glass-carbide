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
from PySide2.QtWidgets import QApplication, QFrame, QVBoxLayout, QHBoxLayout, QLabel, QStackedWidget, QPushButton
from GC_Services.FileIo import FileIo
from ExistingDirectoryView import ExistingDirectoryView
from GC_Views.GCCreateDirectoryView import GCCreateDirectoryView
from GC_Views.GCLogoView import GCLogoView


class GCHomeView(QFrame):
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
        self.lv_logo = GCLogoView()
        self.lbl_instructions = QLabel("Overview of Instructions")

        self.btn_start = QPushButton("Start")
        self.btn_open = QPushButton("Open Existing")
        self.btn_exit = QPushButton("Exit")

        # Setup vbl_left_layout
        self.vbl_left_layout.addWidget(self.lv_logo, alignment=Qt.AlignHCenter)
        self.vbl_left_layout.addWidget(self.lbl_instructions, alignment=Qt.AlignHCenter)
        self.vbl_left_layout.addWidget(self.btn_start)
        self.vbl_left_layout.addWidget(self.btn_open)
        self.vbl_left_layout.addWidget(self.btn_exit)

        # Assign methods for buttons
        self.btn_start.clicked.connect(self.set_new_project_frame)
        self.btn_open.clicked.connect(self.set_existing_project_frame)
        self.btn_exit.clicked.connect(lambda: self.topLevelWidget().close())

        # --------------------------------------------------
        # -----------------vbl_right_layout-----------------
        # --------------------------------------------------

        self.vbl_right_layout = QVBoxLayout()

        # Initialize vbl_right_layout GUI Elements
        self.sw_project_setup = QStackedWidget()

        # Initialize Directory Mapping Views
        self.frm_blank = QFrame()
        self.dmv_mapping_view = GCCreateDirectoryView(None, file_io=self.fio)
        self.edv_existing_view = ExistingDirectoryView(None)

        # Add views to sw_project_setup
        self.sw_project_setup.addWidget(self.frm_blank)
        self.sw_project_setup.addWidget(self.dmv_mapping_view)
        self.sw_project_setup.addWidget(self.edv_existing_view)

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



