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
import asyncio
import sys

from GC_Config import main_config
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QApplication, QWidget, QMainWindow, QAction, QFileDialog, QTableWidget, QTableWidgetItem, QHBoxLayout, \
    QMessageBox

from GC_Views.DirectoryMappingView import DirectoryMappingView
from GC_Views.LogoView import LogoView


class AppWindow(QMainWindow):
    """AppWindow

        Inherits:
            QMainWindow
        Purpose:
            Main Application Window
        Attributes:
            data, headers, data_table
        Methods:
            initUI, init_menus, open_csv, load_data_table
    """

    def __init__(self, parent=None):
        """Constructor

            Parameters:
                self,
                parent
            Returns:
                None
            Purpose:
                Initialize main window and its elements
        """
        super(AppWindow, self).__init__(parent)
        self.data = []
        self.shotdata = []
        self.headers = []
        self.shotheaders = []
        self.data_table = QTableWidget()
        self.shot_table = QTableWidget()
        self.logo = LogoView()

        # Set window parameters
        self.config = main_config.MainWindow()
        self.setWindowTitle(self.config.title)
        self.setGeometry(self.config.left, self.config.top, self.config.width, self.config.height)

        # Set Central Widget
        self.init_ui()

    def init_ui(self):
        """init_ui

            Parameters:
                self
            Returns:
                None
            Purpose:
                Call helper functions to setup gui elements and set central widget
        """
        self.init_menus()
        self.setCentralWidget(self.logo)
        self.show()

    def init_menus(self):
        """init_menus

            Parameters:
                self
            Returns:
                None
            Purpose:
                Initialize menu bar
        """

        main_menu = self.menuBar()

        # File Menu
        file_menu = main_menu.addMenu('File')

        # Open button
        open_button = QAction(QIcon('exit24.png'), 'Open', self)
        open_button.setShortcut('Ctrl+O')
        open_button.setStatusTip('Open CSV')
        open_button.triggered.connect(self.open_csv)

        # Exit Button
        exit_button = QAction(QIcon('exit24.png'), 'Exit', self)
        exit_button.setShortcut('Ctrl+Q')
        exit_button.setStatusTip('Exit application')
        exit_button.triggered.connect(self.close)

        file_menu.addAction(open_button)
        file_menu.addAction(exit_button)

    def display_splash_screen(self):
        pass

    def open_csv(self):
        widge = QWidget()
        hbox = QHBoxLayout()
        qmsgbx = QMessageBox()
        qmsgbx.setText("Select the Assets CSV")
        qmsgbx.exec_()
        asyncio.run(self.read_csv())
        asyncio.run(self.load_data_table())
        qmsgbx.setText("Select the Shots CSV")
        qmsgbx.exec_()
        asyncio.run(self.read_shotcsv())
        asyncio.run(self.load_shot_table())
        hbox.addWidget(self.data_table)
        hbox.addWidget(self.shot_table)
        widge.setLayout(hbox)
        self.setCentralWidget(widge)
        # self.setCentralWidget(self.data_table)

    async def read_csv(self):
        """open_csv
            Purpose:
                Opens and reads csv file into the data array attribute
            Parameters:
                self
            Returns:
                None

        """
        # Get file path and open file in read mode
        file_name = QFileDialog.getOpenFileName(self, "Open CSV Files", "c\\", 'CSV Format (*.csv)')
        filepath = file_name[0]
        csv_file = open(filepath, "r")

        # Grab first two lines as headers
        line = csv_file.readline().split(",")
        line.pop()
        self.headers.append(line)

        line = csv_file.readline().split(",")
        line.pop()
        self.headers.append(line)

        # Dump the rest into the data array
        while (line := csv_file.readline()) != "":
            row = line.replace("\n", "").split(",")
            self.data.append(row)

        csv_file.close()

    async def read_shotcsv(self):
        """open_csv
            Purpose:
                Opens and reads csv file into the data array attribute
            Parameters:
                self
            Returns:
                None

        """
        # Get file path and open file in read mode
        file_name = QFileDialog.getOpenFileName(self, "Open CSV Files", "c\\", 'CSV Format (*.csv)')
        filepath = file_name[0]
        csv_file = open(filepath, "r")

        # Grab first two lines as headers
        line = csv_file.readline().split(",")
        line.pop()
        self.shotheaders.append(line)

        line = csv_file.readline().split(",")

        self.shotheaders.append(line)

        # Dump the rest into the data array
        while (line := csv_file.readline()) != "":
            row = line.replace("\n", "").split(",")
            self.shotdata.append(row)

        csv_file.close()

    async def load_data_table(self):
        """load_data_table

            Parameters:
                self
            Returns:
                None
            Purpose:
                Resizes data_table and fills the table with csv contents
        """
        data_height = len(self.data)
        data_width = len(self.data[0])

        self.data_table.setRowCount(data_height)
        self.data_table.setColumnCount(data_width)

        self.data_table.setHorizontalHeaderLabels(self.headers[1])

        for y in range(len(self.data)):
            for x in range(len(self.data[y])):
                cell = QTableWidgetItem(self.data[y][x])
                self.data_table.setItem(y, x, cell)

        self.data_table.resizeColumnsToContents()

    async def load_shot_table(self):
        """load_data_table

            Parameters:
                self
            Returns:
                None
            Purpose:
                Resizes data_table and fills the table with csv contents
        """
        data_height = len(self.shotdata)
        data_width = len(self.shotdata[0])

        self.shot_table.setRowCount(data_height)
        self.shot_table.setColumnCount(data_width)

        self.shot_table.setHorizontalHeaderLabels(self.shotheaders[1])

        for y in range(len(self.shotdata)):
            for x in range(len(self.shotdata[y])):
                cell = QTableWidgetItem(self.shotdata[y][x])

                self.shot_table.setItem(y, x, cell)

        self.shot_table.resizeColumnsToContents()


if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    aw = AppWindow()
    aw.show()

    dmv = DirectoryMappingView()
    dmv.show()

    sys.exit(qApp.exec_())
