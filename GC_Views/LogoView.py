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

from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QFrame, QLabel, QVBoxLayout


class LogoView(QFrame):
    def __init__(self, parent=None):
        super(LogoView, self).__init__(parent)

        self.logo = QLabel(self)
        pixmap = QPixmap('../GC_Images/logo.png')
        self.logo.setPixmap(pixmap)

        self.main_layout = QVBoxLayout()

        self.main_layout.addWidget(self.logo)
        self.setLayout(self.main_layout)
