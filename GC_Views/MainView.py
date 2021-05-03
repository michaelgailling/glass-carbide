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
from GC_Services.FileIo import FileIo

from PySide2.QtWidgets import QApplication, QMainWindow, QFrame, QStatusBar, QVBoxLayout
from TabView import TabView
from GC_Components.MainComponents import MenuBar


class MainView(QMainWindow):
    def __init__(self, parent=None):
        super(MainView, self).__init__(parent)
        self.layout = QVBoxLayout()
        self.tabFrame = QFrame()
        self.fio = FileIo()
        self.tab_widget = TabView(self, self.fio)
        self.tabIndex = self.tab_widget.tabIndex

        # self.results = []

        # Menu Bar
        self.menuBar = MenuBar(self)
        self.setMenuBar(self.menuBar)

        # Status Bar
        self.statusBar = QStatusBar()
        self.statusBar.showMessage("This is a status message.", 5000)
        self.setStatusBar(self.statusBar)

        # Main window
        self.layout.addWidget(self.tab_widget)
        self.tabFrame.setLayout(self.layout)
        self.setCentralWidget(self.tabFrame)
        self.setWindowTitle("Glass Carbide")
        self.setGeometry(0, 0, 900, 600)
        self.centralWidget().setMinimumSize(900, 600)
        self.setStyleSheet("background-color: white;")
        self.center_screen()

    def center_screen(self):
        screen = self.topLevelWidget().screen().geometry()
        self.resize(screen.width()/1.25, screen.height()/1.5)
        size = self.size()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 3)


if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    mainBase = MainView()
    mainBase.show()
    # directory.show()
    sys.exit(qApp.exec_())
