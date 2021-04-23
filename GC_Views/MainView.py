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
from PySide2.QtWidgets import QApplication, QMainWindow, QAction, QFrame, QStatusBar, QPushButton, QVBoxLayout, \
    QHBoxLayout, QLabel, QMessageBox
from TabView import TabView


class MainView(QMainWindow):
    def __init__(self, parent=None):
        super(MainView, self).__init__(parent)
        self.layout = QVBoxLayout()
        self.tabFrame = QFrame()
        self.tab_widget = TabView()

        # Menu Bar
        self.main_menu = self.menuBar()
        self.main_menu.setStyleSheet("background-color: #E4F3F5")
        # File Menu
        self.file_menu = self.main_menu.addMenu('File')
        # Open button
        self.open_button = QAction(QIcon('exit24.png'), 'Open', self)
        self.open_button.setShortcut('Ctrl+O')
        self.open_button.setStatusTip('Open')
        # New Button
        self.new_button = QAction(QIcon('exit24.png'), 'New', self)
        self.new_button.setShortcut('Ctrl+N')
        self.new_button.setStatusTip('New')
        # new_button.triggered.connect()
        # Save Button
        self.save_button = QAction(QIcon('exit24.png'), 'Save', self)
        self.save_button.setShortcut('Ctrl+S')
        self.save_button.setStatusTip('Save')
        # save_button.triggered.connect()
        # Exit Button
        self.exit_button = QAction(QIcon('exit24.png'), 'Exit', self)
        self.exit_button.setShortcut('Ctrl+Q')
        self.exit_button.setStatusTip('Exit application')
        self.exit_button.triggered.connect(self.close)
        # Add actions to file menu
        self.file_menu.addAction(self.new_button)
        self.file_menu.addAction(self.open_button)
        self.file_menu.addAction(self.save_button)
        self.file_menu.addAction(self.exit_button)

        # Status Bar
        self.statusBar = QStatusBar()
        self.statLbl = QLabel("")
        self.statusBar.showMessage("This is a status message.", 5000)
        self.setStatusBar(self.statusBar)

        # Buttons Container
        self.btnBox = QHBoxLayout()
        self.continueBtn = QPushButton("Continue")
        self.continueBtn.setStyleSheet("background-color:rgb(85,0,255); color:rgb(255,255,255);margin:1 23;padding:10;"
                                       "border:2px solid blue;border-radius:20px")
        self.continueBtn.clicked.connect(self.continue_clicked)
        self.cancelBtn = QPushButton("Cancel")
        self.cancelBtn.setStyleSheet("margin:1 23;color:rgb(85,0,255); background-color:rgb(255,255,255);"
                                     "padding:10;border:2px solid blue;border-radius:20px")
        self.cancelBtn.clicked.connect(self.cancel_clicked)
        self.btnBox.addWidget(self.statLbl)
        self.btnBox.addWidget(self.statLbl)
        self.btnBox.addWidget(self.cancelBtn)
        self.btnBox.addWidget(self.continueBtn)

        # Main window
        self.layout.addWidget(self.tab_widget)
        self.layout.addItem(self.btnBox)
        self.tabFrame.setLayout(self.layout)
        self.setCentralWidget(self.tabFrame)
        self.setWindowTitle("Glass Carbide")
        self.setGeometry(100, 100, 800, 600)
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
