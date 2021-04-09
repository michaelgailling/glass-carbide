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
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QApplication, QTabWidget, QMainWindow, QAction, QFrame, QStatusBar, QDesktopWidget, \
    QPushButton, QVBoxLayout, QHBoxLayout, QLabel
from requests import *
from TableView import TableView


class TabView(QFrame):
    def __init__(self, parent=None):
        super(TabView, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        # Tab Widget
        self.tabWidget = QTabWidget()
        self.step1 = QFrame()
        self.step3 = QFrame()
        # self.tabWidget.width()

        self.tabWidget.setStyleSheet("QTabBar::tab { height: 25%; width: 251%;\n"
                                     "border: 2px solid rgb(0, 0, 205); background-color: rgb(255, 255, 255);\n"
                                     "color: rgb(0, 0, 205); border-bottom:none; margin-left: 2px;}")
        self.tabWidget.addTab(self.step1, "Step 1")
        self.tabWidget.addTab(self.step3, "Step 3")

        self.layout.addWidget(self.tabWidget)
        self.setLayout(self.layout)
        self.setGeometry(0, 0, 800, 500)

    def set_tab_frame(self, frame: QFrame, index_num: int):
        self.tabWidget.insertTab(index_num, frame, "Step 2")


class MainView(QMainWindow):
    def __init__(self, parent=None):
        super(MainView, self).__init__(parent)

        # Menu Bar
        main_menu = self.menuBar()
        main_menu.setStyleSheet("background-color: #E4F3F5")

        # File Menu
        file_menu = main_menu.addMenu('File')
        # Open button
        open_button = QAction(QIcon('exit24.png'), 'Open', self)
        open_button.setShortcut('Ctrl+O')
        open_button.setStatusTip('Open')
        # open_button.triggered.connect)
        # New Button
        new_button = QAction(QIcon('exit24.png'), 'New', self)
        new_button.setShortcut('Ctrl+N')
        new_button.setStatusTip('New')
        # new_button.triggered.connect()
        # Save Button
        save_button = QAction(QIcon('exit24.png'), 'Save', self)
        save_button.setShortcut('Ctrl+S')
        save_button.setStatusTip('Save')
        # save_button.triggered.connect()
        # Exit Button
        exit_button = QAction(QIcon('exit24.png'), 'Exit', self)
        exit_button.setShortcut('Ctrl+Q')
        exit_button.setStatusTip('Exit application')
        exit_button.triggered.connect(self.close)
        # Add actions to file menu
        file_menu.addAction(new_button)
        file_menu.addAction(open_button)
        file_menu.addAction(save_button)
        file_menu.addAction(exit_button)

        # Status Bar
        self.statusBar = QStatusBar()
        self.statLbl = QLabel("Status Bar")
        self.statusBar.showMessage("This is an status message.", 5000)
        # self.statusBar.addPermanentWidget(self.statLbl)
        # Buttons Container
        self.hbox = QHBoxLayout()
        self.continueBtn = QPushButton("Continue")
        self.continueBtn.setStyleSheet("background-color:rgb(85,0,255); color:rgb(255,255,255);")
        self.cancelBtn = QPushButton("Cancel")
        self.cancelBtn.setStyleSheet("color:rgb(85,0,255); background-color:rgb(255,255,255);")
        self.hbox.addWidget(self.continueBtn)
        self.hbox.addWidget(self.cancelBtn)
        # self.btnBar.addWidget(self.continueBtn)

        # Main window
        self.setWindowTitle("Glass Carbide")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: white")
        self.center_screen()

    def center_screen(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)


if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    mainBase = MainView()
    table = TableView()
    tabs = TabView()
    tabs.set_tab_frame(table, 1)
    mainBase.setCentralWidget(tabs)
    mainBase.show()
    sys.exit(qApp.exec_())
