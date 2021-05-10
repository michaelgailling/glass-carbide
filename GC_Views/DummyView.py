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

from PySide2.QtGui import Qt
from PySide2.QtWidgets import QFrame, QApplication, QVBoxLayout

from GC_Components.TableComponents import DataTable


class DummyView(QFrame):
    def __init__(self, width=3, height=3, parent=None):
        super(DummyView, self).__init__(parent)
        self.vBox = QVBoxLayout()

        self.table = DataTable()
        self.vBox.addWidget(self.table)
        self.setLayout(self.vBox)

    def table_loader(self, results=[]):
        if results:
            headers = results.pop(0)
            self.table.load_table(results)
            self.table.set_headers(headers)

