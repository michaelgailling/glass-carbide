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

from GC_Components.InputComponents import LabeledDirectoryInput


class ResultsOutputView(QFrame):
    def __init__(self, parent=None):
        super(ResultsOutputView, self).__init__(parent)
        self.layout = QVBoxLayout()
        self.grid = QGridLayout()

        # Label
        self.displayLbl = QLabel("Review")

        # Root Directory Mapping input
        self.project_dir = LabeledDirectoryInput(self, label_text="Project Folder: ")

        # Combo Boxes
        self.softwareBox = QComboBox(self)
        self.softwareBox.addItem("Select Software   ...")
        self.softwareBox.setStyleSheet('background-color:white;padding:6 6')
        self.comboBox = QVBoxLayout()
        self.comboBox.setSpacing(1)

        # Results Display
        self.resultFrame = QFrame()
        self.resultFrame.setStyleSheet('border:2px solid blue; margin:0 5; background-color:white;')

        # Layout Loading
        self.comboBox.addWidget(self.project_dir)
        self.comboBox.addWidget(self.softwareBox, alignment=Qt.AlignHCenter)
        self.layout.addWidget(self.resultFrame)
        self.layout.addItem(self.comboBox)
        self.layout.setContentsMargins(30, 20, 30, 30)
        self.setLayout(self.layout)

        self.setGeometry(0, 0, 800, 500)

    def set_result_frame(self, results_data_frame: QVBoxLayout):
        self.resultFrame.setLayout(results_data_frame)


if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    resOut = ResultsOutputView()
    resOut.show()
    sys.exit(qApp.exec_())
