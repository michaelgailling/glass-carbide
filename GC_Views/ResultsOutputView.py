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
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QComboBox, QFrame, QVBoxLayout, QLabel, QGridLayout


class ResultsOutputView(QFrame):
    def __init__(self, parent=None):
        super(ResultsOutputView, self).__init__(parent)
        self.layout = QVBoxLayout()
        self.grid = QGridLayout()

        # Label
        self.displayLbl = QLabel("Review")

        # Combo Boxes
        self.episodeBox = QComboBox(self)
        self.episodeBox.addItem("Select Episode   ...")
        self.episodeBox.setStyleSheet('background-color:white;padding:6 6')
        self.softwareBox = QComboBox(self)
        self.softwareBox.addItem("Select Software   ...")
        self.softwareBox.setStyleSheet('background-color:white;padding:6 6')
        self.comboBox = QVBoxLayout()
        self.comboBox.setSpacing(15)

        # Results Display
        self.resultFrame = QFrame()
        self.resultFrame.setStyleSheet('border:2px solid blue; margin: 5; background-color:white;')

        # Layout Loading
        self.comboBox.addWidget(self.episodeBox, alignment=Qt.AlignHCenter)
        self.comboBox.addWidget(self.softwareBox, alignment=Qt.AlignHCenter)
        self.layout.addWidget(self.resultFrame)
        self.layout.addItem(self.comboBox)
        self.layout.setContentsMargins(50, 20, 50, 50)
        self.setLayout(self.layout)

        self.setGeometry(0, 0, 800, 500)


if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    resOut = ResultsOutputView()
    resOut.show()
    sys.exit(qApp.exec_())
