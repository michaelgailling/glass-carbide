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
        self.setStyleSheet("background-color: white")
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
        if self.tab_widget.tabWidget.currentIndex() < 2:
            self.tab_widget.tabWidget.setCurrentIndex(self.tab_widget.tabWidget.currentIndex() + 1)
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Are you sure?")
            msg.setText("Open { Project Name } in { Software }?")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.exec_()

    def cancel_clicked(self):
        if self.tab_widget.tabWidget.currentIndex() >= 1:
            self.tab_widget.tabWidget.setCurrentIndex(self.tab_widget.tabWidget.currentIndex() - 1)
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Save your progress?")
            msg.setText("Would you like to save your progress?")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Save | QMessageBox.Cancel | QMessageBox.Close)

            msg.exec_()


if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    mainBase = MainView()
    mainBase.show()
    # directory.show()
    sys.exit(qApp.exec_())
