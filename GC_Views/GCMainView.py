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
from PySide2.QtWidgets import QApplication, QMainWindow

from GC_Views.GCTabView import GCTabView



class GCMainView(QMainWindow):
    """GC Main View

        Summary:
            A class for {Type} that includes:

            -{Description} to the {Location eg left}

        Attributes:
            menuBar, statusBar, fio, tab_widget

        Methods:
            center_screen

        Attributes
        ----------
            fio : FileIo
                !!! File input & output
            tab_widget : TabView
                Tab View for tabs/steps

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

        self.tab_widget = GCTabView(self, self.fio)
        self.tab_widget.setObjectName('tab')

        # Main window
        self.setCentralWidget(self.tab_widget)
        self.centralWidget().setContentsMargins(0, 0, 0, 0)

        # Styling
        self.centralWidget().setMinimumSize(900, 600)
        # self.centralWidget().topLevelWidget().setStyleSheet('border:3px solid #1000A0;font-weight:600')
        # self.topLevelWidget().setStyleSheet('QFrame#tab{border-top:1.1px solid #1000A0;border-bottom:none;'
        #                                     'border-left:2px solid #1000A0;border-right:2px solid #1000A0;'
        #                                     'margin:0;background-color:white;}')
        self.center_screen()

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
