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
from PySide2.QtWidgets import QApplication, QFrame, QPushButton, QVBoxLayout


class GCHomeBtnsView(QFrame):
    """Home Buttons View

        Summary:
            A class for {Type} that includes:

            -{Description} to the {Location eg left}

        Attributes:
            btnBox, startBtn, openBtn, exitBtn

        Methods:
            None

        Attributes
        ----------
            btnBox : QVBoxLayout
                Layout vertically stacks buttons
            startBtn : QPushButton
                Button for starting new project
            openBtn : QPushButton
                Button for opening existing project
            exitBtn : QPushButton
                Button for exiting application

        Methods
        -------
            None
    """
    def __init__(self, parent=None):
        """Constructor:
            Initialize Home Buttons View

            Parameters:
                self
                parent : QFrame
            Returns:
                None
        """
        super(GCHomeBtnsView, self).__init__(parent)
        self.btnBox = QVBoxLayout()

        # Buttons
        self.startBtn = QPushButton("Start")
        self.startBtn.setStyleSheet("background-color:#1000A0; color:rgb(255,255,255);margin:0 15; padding:10 5;"
                                    "border:2px solid #1000A0;border-radius:20px;")
        self.openBtn = QPushButton("Open Existing")
        self.openBtn.setStyleSheet("background-color:#1000A0; color:rgb(255,255,255);margin:0 15; padding:10 5;"
                                    "border:2px solid #1000A0;border-radius:20px;")
        self.exitBtn = QPushButton("Exit")
        self.exitBtn.setStyleSheet("color:#1000A0; background-color:rgb(255,255,255);border:2px solid #1000A0;"
                                   "border-radius:20px; padding:10 5;margin:0 15")
        self.exitBtn.clicked.connect(lambda: self.topLevelWidget().close())

        self.btnBox.addWidget(self.startBtn)
        self.btnBox.addWidget(self.openBtn)
        self.btnBox.addWidget(self.exitBtn)

        self.setLayout(self.btnBox)


if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    hom = GCHomeBtnsView()
    hom.show()
    sys.exit(qApp.exec_())

