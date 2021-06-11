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
from PySide2.QtGui import QPixmap, QFont
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
                            lbl_thumbnail, btn_include, btn_ignore, img_btn_frame

                        Methods:
                            None

                        Attributes
                        ----------
                            hbl_main_layout : QHBoxLayout
                                Main horizontal layout
                            vbl_img_btns_layout : QVBoxLayout
                                Vertical layout for image & buttons
                            lbl_details : QLabel
                                Label for file details text
                            dt_table : DataTable
                                Data Table for list of duplicates
                            lbl_thumbnail : QLabel
                                Label for thumbnail image
                            btn_include = QPushButton
                                Button for including file in download
                            btn_ignore = QPushButton
                                Button for ignoring file in download
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

        # File details Label
        self.lbl_details = QLabel("Files Details")
        self.lbl_details.setObjectName("details")
        self.lbl_details.setAlignment(Qt.AlignCenter)

        # Table of Files with Duplicates
        self.dt_file_list = DataTable(self)
        self.dt_file_list.set_dimensions(1, 0)
        self.dt_file_list.table.cellDoubleClicked.connect(self.file_table_cell_clicked)

        # Vertical Box for File details
        self.vbl_details = QVBoxLayout()
        self.vbl_details.addWidget(self.dt_file_list)
        self.vbl_details.addWidget(self.lbl_details)

        # PixMap for file thumbnail
        self.lbl_thumbnail = QLabel(self)
        self.lbl_thumbnail.setObjectName("thumbnail")

        # Buttons
        self.btn_include = QPushButton("Include File")
        self.btn_include.clicked.connect(self.include_file)
        self.btn_ignore = QPushButton("Ignore File")
        self.btn_ignore.clicked.connect(self.ignore_file)

        # Vertical Layout Adding
        self.img_btn_frame = QFrame()
        self.img_btn_frame.setStyleSheet('::section{background-color:white}')
        self.vbl_img_btns_layout.addWidget(self.lbl_thumbnail, alignment=Qt.AlignCenter)
        self.vbl_img_btns_layout.addWidget(self.btn_include, alignment=Qt.AlignHCenter)
        self.vbl_img_btns_layout.addWidget(self.btn_ignore, alignment=Qt.AlignHCenter)
        self.img_btn_frame.setLayout(self.vbl_img_btns_layout)
        self.img_btn_frame.setObjectName("picArea")

        # Main Layout
        self.hbl_main_layout.addLayout(self.vbl_details)
        self.hbl_main_layout.addWidget(self.img_btn_frame, stretch=1)
        self.setLayout(self.hbl_main_layout)

        # Styling
        self.setGeometry(133, 133, 1000, 600)
        self.setObjectName('dupePop')
        self.setStyleSheet('QFrame{border:1px solid #1000A0;background-color:#e6e6e6;padding:0;margin:1px;}'
                           'DataTable{background-color:#1000A0} QHBoxLayout#mainbox{background-color:#e6e6e6}'
                           'QLabel#details{background-color:white;color:#1000A0;font-family:Arial;font-size:15}'
                           'QTableWidget{background-color:white;font-weight:600} QFrame#picArea{background-color:white}'
                           'QPushButton{font-weight:600;background-color:#1000A0;border-radius:20px;'
                           'padding:10 133;color:rgb(255,255,255);margin:1 30;border:2px solid #1000A0;}')

        self.setStyleSheet('background-color:#e6e6e6')

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
                                                     size="1024x512")

            pixmap.loadFromData(thumbnail)
            pixmap = pixmap.scaledToWidth(self.img_btn_frame.width()-13)
            self.lbl_thumbnail.setPixmap(pixmap)
        else:
            file_extension = self.selected_file.name[-4:]
            if "wav" in file_extension:
                pixmap = QPixmap('../GC_Images/wavicon.png').scaledToWidth(400)
                self.lbl_thumbnail.setPixmap(pixmap)
            elif "fla" in file_extension:
                pixmap = QPixmap('../GC_Images/flaicon.png').scaledToWidth(400)
                self.lbl_thumbnail.setPixmap(pixmap)
            elif "png" in file_extension:
                pixmap = QPixmap('../GC_Images/pngicon.png').scaledToWidth(400)
                self.lbl_thumbnail.setPixmap(pixmap)
            elif "mp4" in file_extension:
                pixmap = QPixmap('../GC_Images/mp4icon.png').scaledToWidth(400)
                self.lbl_thumbnail.setPixmap(pixmap)
            elif "psd" in file_extension:
                pixmap = QPixmap('../GC_Images/psdicon.png').scaledToWidth(400)
                self.lbl_thumbnail.setPixmap(pixmap)
            else:
                pixmap = QPixmap()
            self.lbl_thumbnail.setPixmap(pixmap)
            self.lbl_thumbnail.resize(self.img_btn_frame.width(), self.img_btn_frame.height())

    def include_file(self):
        pass

    def ignore_file(self):
        pass


if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    mainBase = FileDetailsView()
    mainBase.show()
    sys.exit(qApp.exec_())
