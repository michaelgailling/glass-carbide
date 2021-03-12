# Project Name:
# Glass Carbide
#
# By:
# Michael Gailling
# Mustafa Butt
#
# Organization:
# WIMTACH
#

import sys
import config
import csv
from PySide2 import QtCore
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QApplication, QWidget, QTabWidget, QMainWindow, QAction, QFrame, QPlainTextEdit, \
    QSplitter, QVBoxLayout, QFileDialog, QTableWidget, QTableWidgetItem


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class AppWindow(QMainWindow):
    data_table = []
    header = []

    def __init__(self, parent=None):
        super(AppWindow, self).__init__(parent)
        mainConfig = config.MainWindow()
        # Define constants
        self.title = 'glass-carbide'
        self.left = 100
        self.top = 100
        self.width = 640
        self.height = 400

        # Set window parameters
        self.setWindowTitle(mainConfig.title)
        self.setGeometry(mainConfig.left, mainConfig.top, mainConfig.width, mainConfig.height)


        # Set Central Widget
        self.data_table_widget = QTableWidget()
        self.setCentralWidget(self.data_table_widget)
        self.initUI()

    def initUI(self):
        main_menu = self.menuBar()



        file_menu = main_menu.addMenu('File')
        
        exit_button = QAction(QIcon('exit24.png'), 'Exit', self)
        exit_button.setShortcut('Ctrl+Q')
        exit_button.setStatusTip('Exit application')
        exit_button.triggered.connect(self.close)
        open_button = QAction(QIcon('exit24.png'), 'Open', self)
        open_button.setShortcut('Ctrl+O')
        open_button.setStatusTip('Open CSV')
        open_button.triggered.connect(self.open_csv)

        file_menu.addAction(exit_button)
        file_menu.addAction(open_button)

        self.show()

    def build_table(self):
        for y in range(len(self.data_table)):
            for x in range(len(self.data_table[y])):
                self.data_table_widget.setItem(x, y, QTableWidgetItem(self.data_table[y][x]))

    def open_csv(self):
        file_name = QFileDialog.getOpenFileName(self, "Open CSV Files", "c\\",
                                                'CSV Format (*.csv)')
        filepath = file_name[0]
        csv_file = open(filepath, "r")
        line = csv_file.readline()
        self.header = line.split(",")[0]
        while line != "":
            line = csv_file.readline()
            row = line.split(",")
            self.data_table.append(row)

        self.build_table()


if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    aw = AppWindow()
    aw.show()
    sys.exit(qApp.exec_())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
