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
from PySide2.QtWidgets import QFrame

from GC_Components.TableComponents import DataTable


class DummyView(QFrame):
    def __init__(self, width=3, height=3, parent=None):
        super(DummyView, self).__init__(parent)

        self.table = DataTable()

    def table_loader(self, results: []):
        self.table.load_data(results)

