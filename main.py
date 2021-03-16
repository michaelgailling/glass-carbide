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

from PySide2 import QtCore

import config
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QApplication, QWidget, QTabWidget, QMainWindow, QAction, QFrame, QPlainTextEdit, \
    QSplitter, QVBoxLayout, QFileDialog, QTableWidget, QTableWidgetItem, QTableView


class InfoView(QFrame):
    def __init__(self, parent=None):
        super(InfoView, self).__init__(parent)

        # self.IVWV = IVWebView(parent=self, url="https://www.google.com/")
        # self.page = self.IVWV.page()
        # self.source_text = QPlainTextEdit()
        # self.mainViewSplitter = QSplitter(QtCore.Qt.Vertical)

        self.mainViewSplitter.addWidget()
        self.mainViewSplitter.addWidget()
        self.main_layout = QVBoxLayout()

        self.main_layout.addWidget(self.mainViewSplitter)
        self.setLayout(self.main_layout)


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
        self.headers = []
        self.data_table = QTableWidget()

        # Set window parameters
        main_config = config.MainWindow()
        self.setWindowTitle(main_config.title)
        self.setGeometry(main_config.left, main_config.top, main_config.width, main_config.height)

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
        self.setCentralWidget(self.data_table)
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

        # Exit Button
        exit_button = QAction(QIcon('exit24.png'), 'Exit', self)
        exit_button.setShortcut('Ctrl+Q')
        exit_button.setStatusTip('Exit application')
        exit_button.triggered.connect(self.close)

        # Open button
        open_button = QAction(QIcon('exit24.png'), 'Open', self)
        open_button.setShortcut('Ctrl+O')
        open_button.setStatusTip('Open CSV')
        open_button.triggered.connect(self.open_csv)

        file_menu.addAction(exit_button)
        file_menu.addAction(open_button)

    def open_csv(self):
        """open_csv
            Purpose:
                Opens and reads csv file into the data member var
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

        self.load_data_table()

    def load_data_table(self):
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


if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    aw = AppWindow()
    aw.show()
    sys.exit(qApp.exec_())
