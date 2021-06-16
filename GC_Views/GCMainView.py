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

from GC_Components.MainComponents import MenuBar
from GC_Services.FileIo import FileIo
from PySide2.QtWidgets import QApplication, QMainWindow, QStatusBar, QProgressBar
from GC_Views.GCTabView import GCTabView


class GCMainView(QMainWindow):
    """GC Main View

        Summary:
            A class for Main View of application that includes:

            -Central tab view
            -MenuBar at top
            -StatusBar at bottom left
            -ProgressBar at bottom right

        Attributes:
            menuBar, statusBar, fio, tab_widget, progress_bar,

        Methods:
            center_screen

        Attributes
        ----------
            fio : FileIo
                File input & output
            tab_widget : TabView
                Tab View for tabs/steps
            menuBar : MenuBar
                Menu Bar
            self.statusBar : QStatusBar
                Status Bar
            progress_bar : QProgressBar
                Progress Bar for download progress

        Methods
        -------
            center_screen(self)
                Positions application in center of screen
    """
    def __init__(self, parent=None):
        """Constructor:
            Initialize Main View

            Parameters:
                self
                parent : QMainWindow
            Returns:
                None
        """
        # -------------------------------------------init Start-------------------------------------------
        super(GCMainView, self).__init__(parent)
        self.fio = FileIo()

        # Main window config
        self.setWindowTitle("Glass Carbide")
        self.setGeometry(0, 0, 900, 600)

        # Tab Widget
        self.tab_widget = GCTabView(self, self.fio)

        # Menu Bar
        self.menuBar = MenuBar(self)
        self.setMenuBar(self.menuBar)

        # Status Bar
        self.statusBar = QStatusBar()
        self.statusBar.showMessage("This is a status message.", 5000)
        self.setStatusBar(self.statusBar)
        self.statusBar.setStyleSheet('QStatusBar{border:1px solid #1000A0;background-color:#e6e6e6;border-top:none;}')

        # Progress Bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(100)
        self.progress_bar.setValue(0)
        self.statusBar.addPermanentWidget(self.progress_bar)

        # Main window
        self.setCentralWidget(self.tab_widget)
        self.centralWidget().setContentsMargins(-3, -3, -3, -3)

        # Styling
        self.centralWidget().setMinimumSize(900, 600)
        self.center_screen()
        self.topLevelWidget().setStyleSheet('QMainWindow{background-color:white;border:1px solid #1000A0;}'
                                            'MenuBar{border-bottom:1px solid #1000A0;background-color:#e6e6e6;}'
                                            'QLabel{font-weight:600} QLineEdit{border:1px solid #1000A0}'
                                            'QPushButton{font-weight:600;background-color:#1000A0;border-radius:20px;'
                                            'padding:10;color:rgb(255,255,255);margin:1 5;border:2px solid #1000A0;}')

        # -------------------------------------------init End-------------------------------------------

    def center_screen(self):
        screen = self.topLevelWidget().screen().geometry()
        self.resize(screen.width()/1.25, screen.height()/1.5)
        size = self.size()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 3)


if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    mainBase = GCMainView()
    mainBase.show()
    sys.exit(qApp.exec_())
