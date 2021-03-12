import sys
import config
from PySide2 import QtCore
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QApplication, QWidget, QTabWidget, QMainWindow, QAction, QFrame, QPlainTextEdit, \
    QSplitter, QVBoxLayout

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class AppWindow(QMainWindow):
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

        self.initUI()


    def initUI(self):
        main_menu = self.menuBar()

        file_menu = main_menu.addMenu('File')

        exit_button = QAction(QIcon('exit24.png'), 'Exit', self)
        exit_button.setShortcut('Ctrl+Q')
        exit_button.setStatusTip('Exit application')
        exit_button.triggered.connect(self.close)
        file_menu.addAction(exit_button)


        self.show()


if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    aw = AppWindow()
    aw.show()
    sys.exit(qApp.exec_())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
