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
from PySide2.QtWidgets import QFrame, QHBoxLayout, QFileDialog, QPushButton, QMessageBox, QVBoxLayout, QApplication, \
    QTextBrowser, QLabel
from GC_Components.InputComponents import LabeledDirectoryInput
from GC_Components.TableComponents import DataTable
from GC_Services.FileIo import FileIo


class FileDetailsView(QFrame):
    """File Details View

                        Summary:
                            A class for {Type} that includes:

                            -{Description} to the {Location eg left}

                        Attributes:
                            hbl_main_layout, vbl_img_btns_layout, lbl_duplicates, lbl_details, lbl_thumbnail, dt_table,
                            tb_details, lbl_thumbnail, btn_check, btn_change, img_btn_frame

                        Methods:
                            None

                        Attributes
                        ----------
                            hbl_main_layout : QHBoxLayout
                                Main horizontal layout
                            vbl_img_btns_layout : QVBoxLayout
                                Vertical layout for image & buttons
                            lbl_duplicates : QLabel
                                Label for duplicates
                            lbl_details : QLabel
                                Label for details
                            lbl_thumbnail : QLabel
                                Label for thumbnail
                            dt_table : DataTable
                                Data Table for list of duplicates
                            tb_details : QTextBrowser
                                Text Browser for File details
                            lbl_thumbnail : QLabel
                                Label for thumbnail image
                            btn_check = QPushButton
                                Button for
                            btn_change = QPushButton
                                Button for
                            img_btn_frame = QFrame
                                QFrame to display thumbnail image and buttons

                        Methods
                        -------
                            None

                    """

    def __init__(self, parent=None):
        """Constructor:
            Initialize Directory Mapping View

            Parameters:
                self
                parent : QFrame
            Returns:
                None
        """
        super(FileDetailsView, self).__init__(parent)
        self.hbl_main_layout = QHBoxLayout()
        self.vbl_img_btns_layout = QVBoxLayout()

        # Identifier Labels
        self.lbl_duplicates = QLabel("List of Files with Duplicates")
        self.lbl_details = QLabel("Files Details")
        self.lbl_thumbnail = QLabel("List of Files with Duplicates")

        # Table of Files with Duplicates
        self.dt_table = DataTable(self)

        # Text Browser for File details
        self.tb_details = QTextBrowser()

        # PixMap for file thumbnail
        self.lbl_thumbnail = QLabel(self)
        self.lbl_thumbnail.setStyleSheet('QFrame{border:3px solid #1000A0;}')

        # Buttons
        self.btn_check = QPushButton("Check")
        self.btn_change = QPushButton("Change")

        # Vertical Layout Adding
        self.img_btn_frame = QFrame()
        self.img_btn_frame.setStyleSheet('::section{background-color:white}')
        self.vbl_img_btns_layout.addWidget(self.lbl_thumbnail)
        self.vbl_img_btns_layout.addWidget(self.btn_change)
        self.vbl_img_btns_layout.addWidget(self.btn_check)
        self.img_btn_frame.setLayout(self.vbl_img_btns_layout)

        # Main Layout
        self.hbl_main_layout.addWidget(self.dt_table)
        self.hbl_main_layout.addWidget(self.tb_details)
        self.hbl_main_layout.addWidget(self.img_btn_frame, stretch=1)
        self.setLayout(self.hbl_main_layout)

        # Styling
        self.setGeometry(133, 133, 1000, 600)
        self.setObjectName('dupePop')
        self.setStyleSheet('background-color:#e6e6e6')
        self.setStyleSheet('QFrame{border:2px solid #1000A0;background-color:#e6e6e6;padding:0;margin:0;}'
                           'DataTable{background-color:#1000A0} QHBoxLayout#mainbox{background-color:#e6e6e6}'
                           'QTextBrowser{background-color:white}QLabel{background-color:white}'
                           'QTableWidget{background-color:white;font-weight:600}'
                           'QPushButton{font-weight:600;background-color:#1000A0;border-radius:20px;'
                           'padding:10;color:rgb(255,255,255);margin:1 33;border:2px solid #1000A0;}')


if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    mainBase = FileDetailsView()
    mainBase.show()
    sys.exit(qApp.exec_())
