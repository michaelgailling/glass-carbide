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
from PySide2.QtWidgets import QApplication, QMainWindow, QAction, QFrame, QStatusBar, QPushButton, QVBoxLayout, \
    QHBoxLayout, QLabel, QMessageBox
from TabView import TabView
from GC_Components.MainComponents import MenuBar, MainButtons


class MainView(QMainWindow):
    def __init__(self, parent=None):
        super(MainView, self).__init__(parent)
        self.layout = QVBoxLayout()
        self.tabFrame = QFrame()
        self.tab_widget = TabView()

        self.tabIndex = self.tab_widget.tabIndex

        # Menu Bar
        self.menuBar = MenuBar(self)
        self.setMenuBar(self.menuBar)

        # Status Bar
        self.statusBar = QStatusBar()
        self.statusBar.showMessage("This is a status message.", 5000)
        self.setStatusBar(self.statusBar)

        # Cancel and Continue Buttons
        self.btnBox = MainButtons(self)
        self.btnBox.continueBtn.clicked.connect(self.continue_clicked)
        self.btnBox.cancelBtn.clicked.connect(self.cancel_clicked)

        # Main window
        self.layout.addWidget(self.tab_widget)
        self.layout.addItem(self.btnBox)
        self.tabFrame.setLayout(self.layout)
        self.setCentralWidget(self.tabFrame)
        self.setWindowTitle("Glass Carbide")
        self.setGeometry(100, 100, 900, 600)
        self.centralWidget().setMinimumSize(900, 600)
        self.setStyleSheet("background-color: white;")
        self.center_screen()

    def center_screen(self):
        size = self.size()
        print('Size: %d x %d' % (size.width(), size.height()))
        # rect = self.
        # print('Available: %d x %d' % (rect.width(), rect.height()))
        # screen = QGuiApplication.screenAt()
        # size = self.geometry()
        # self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

    def continue_clicked(self):
        if self.tab_widget.homeView.mappingView.get_dir_path():
            self.tab_widget.dir_getter()

        tabIndex = self.tab_widget.tabIndex

        if tabIndex == self.tab_widget.homeView.tabIndex:
            self.tab_widget.tab_index_setter(self.tab_widget.tableView.tabIndex)
            self.tab_widget.tabIndex = self.tab_widget.tableView.tabIndex
        elif tabIndex == self.tab_widget.tableView.tabIndex:
            self.tab_widget.tab_index_setter(self.tab_widget.previewView.tabIndex)
            self.tab_widget.tabIndex = self.tab_widget.previewView.tabIndex
        elif tabIndex == self.tab_widget.previewView.tabIndex:
            msg = QMessageBox()
            msg.setWindowTitle("Are you sure?")
            msg.setText("Open { Project Name } in { Software }?")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.exec_()
        else:
            pass

    def cancel_clicked(self):
        tabIndex = self.tab_widget.tabIndex

        if tabIndex == self.tab_widget.homeView.tabIndex:
            msg = QMessageBox()
            msg.setWindowTitle("Save your progress?")
            msg.setText("Would you like to save your progress?")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Save | QMessageBox.Cancel | QMessageBox.Close)
            msg.exec_()
        elif tabIndex == self.tab_widget.tableView.tabIndex:
            self.tab_widget.tab_index_setter(self.tab_widget.homeView.tabIndex)
            self.tab_widget.tabIndex = self.tab_widget.homeView.tabIndex
        elif tabIndex == self.tab_widget.previewView.tabIndex:
            self.tab_widget.tab_index_setter(self.tab_widget.tableView.tabIndex)
            self.tab_widget.tabIndex = self.tab_widget.tableView.tabIndex


if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    mainBase = MainView()
    mainBase.show()
    # directory.show()
    sys.exit(qApp.exec_())
