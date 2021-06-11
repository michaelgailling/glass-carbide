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
from PySide2.QtWidgets import QFrame, QHBoxLayout, QFileDialog, QPushButton, QMessageBox, QVBoxLayout, QApplication, \
    QTextBrowser, QLabel, QWidget
from GC_Components.InputComponents import LabeledDirectoryInput
from GC_Components.TableComponents import DataTable
from GC_Models.PCloudFileModel import PCloudFileModel
from GC_Services.FileIo import FileIo


class FileDetailsView(QWidget):
    """File Details View

                        Summary:
                            A class for viewing pcloud file details that includes:

                            -Data Table for list of files to the left
                            -TextBrowser for file details in the center
                            -Frame containing Label for file's thumbnail image & buttons on right

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
        super().__init__()
        self.parent = parent
        self.file_data = []
        self.selected_file = None

        self.hbl_main_layout = QHBoxLayout()
        self.vbl_img_btns_layout = QVBoxLayout()

        # Identifier Labels
        self.lbl_duplicates = QLabel("List of Files with Duplicates")
        self.lbl_details = QLabel("Files Details")
        self.lbl_thumbnail = QLabel("List of Files with Duplicates")

        # Table of Files with Duplicates
        self.dt_file_list = DataTable(self)
        self.dt_file_list.set_dimensions(1, 0)
        self.dt_file_list.table.cellDoubleClicked.connect(self.file_table_cell_clicked)
        # Vertical Box for File details
        self.vbl_details = QVBoxLayout()
        self.vbl_details.addWidget(self.lbl_details)

        # PixMap for file thumbnail
        self.lbl_thumbnail = QLabel(self)
        self.lbl_thumbnail.setStyleSheet('QFrame{border:3px solid #1000A0;}')

        # Buttons
        self.btn_check = QPushButton("Check")
        # self.btn_change = QPushButton("Change")

        # Vertical Layout Adding
        self.img_btn_frame = QFrame()
        self.img_btn_frame.setStyleSheet('::section{background-color:white}')
        self.img_btn_frame.setMaximumWidth(512)
        self.vbl_img_btns_layout.addWidget(self.lbl_thumbnail)
        # self.vbl_img_btns_layout.addWidget(self.btn_change)
        self.vbl_img_btns_layout.addWidget(self.btn_check)
        self.img_btn_frame.setLayout(self.vbl_img_btns_layout)

        # Main Layout
        self.hbl_main_layout.addWidget(self.dt_file_list, stretch=1)
        self.hbl_main_layout.addLayout(self.vbl_details)
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

    def file_table_cell_clicked(self, row=0, column=0):
        filename = self.dt_file_list.get_row(row)[0]
        self.selected_file = None

        for file in self.file_data:
            if file.name == filename:
                self.selected_file = file
                break

        if self.selected_file:
            self.display_file_data()

    def set_file_list(self, file_data=[]):
        self.file_data = file_data

        filenames = []

        for file in file_data:
            filenames.append([file.name])

        self.dt_file_list.load_table(filenames)

    def display_file_data(self):
        self.set_thumbnail()
        self.lbl_details.setText(str(self.selected_file))

    def set_thumbnail(self):
        thumbnail = None
        pixmap = QPixmap()
        self.lbl_thumbnail.clear()
        if self.selected_file.thumb:
            thumbnail = self.parent.apic.getpubthumb(code=self.selected_file.publink_code,
                                                     file_id=self.selected_file.fileid,
                                                     size="512x1024")

            pixmap.loadFromData(thumbnail)
            pixmap = pixmap.scaledToWidth(256)
            self.lbl_thumbnail.setPixmap(pixmap)
        else:
            file_extension = self.selected_file.name[-4:]
            if "wav" in file_extension:
                pixmap = QPixmap('../GC_Images/wavicon.png').scaledToWidth(256)
                self.lbl_thumbnail.setPixmap(pixmap)
            elif "fla" in file_extension:
                pixmap = QPixmap('../GC_Images/flaicon.png').scaledToWidth(256)
                self.lbl_thumbnail.setPixmap(pixmap)
            elif "png" in file_extension:
                pixmap = QPixmap('../GC_Images/pngicon.png').scaledToWidth(256)
                self.lbl_thumbnail.setPixmap(pixmap)
            elif "mp4" in file_extension:
                pixmap = QPixmap('../GC_Images/mp4icon.png').scaledToWidth(256)
                self.lbl_thumbnail.setPixmap(pixmap)
            elif "psd" in file_extension:
                pixmap = QPixmap('../GC_Images/psdicon.png').scaledToWidth(256)
                self.lbl_thumbnail.setPixmap(pixmap)
            else:
                pixmap = QPixmap()
            self.lbl_thumbnail.setPixmap(pixmap)



if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    mainBase = FileDetailsView()
    mainBase.show()
    sys.exit(qApp.exec_())
