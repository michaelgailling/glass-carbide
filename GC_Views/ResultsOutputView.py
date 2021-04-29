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
from GC_Components.TableComponents import DataTable
from GC_Services.FileIo import FileIo


class ResultsOutputView(QFrame):
    def __init__(self, parent=None, file_io=FileIo()):
        super(ResultsOutputView, self).__init__(parent)
        self.layout = QVBoxLayout()
        self.grid = QGridLayout()
        self.data = []
        self.fio = file_io

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
        self.dt_data = DataTable()

        # Layout Loading
        self.comboBox.addWidget(self.project_dir)
        self.comboBox.addWidget(self.softwareBox, alignment=Qt.AlignHCenter)
        self.layout.addWidget(self.dt_data)
        self.layout.addItem(self.comboBox)
        self.layout.setContentsMargins(30, 20, 30, 30)
        self.setLayout(self.layout)

        self.setGeometry(0, 0, 800, 500)

    def load_table_data(self, results=[]):
        try:
            headers = results.pop(0)
            self.dt_data.load_data(results)
            self.dt_data.set_headers(headers)
        except:
            pass

    def set_data(self, data=[]):
        self.data = data


if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    resOut = ResultsOutputView()
    resOut.show()
    sys.exit(qApp.exec_())
