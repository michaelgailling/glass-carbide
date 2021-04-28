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

from PySide2.QtWidgets import QFrame, QApplication, QVBoxLayout

from GC_Components.TableComponents import DataTable


class DummyView(QFrame):
    def __init__(self, width=3, height=3, parent=None):
        super(DummyView, self).__init__(parent)
        self.vBox = QVBoxLayout()

        self.table = DataTable()
        self.vBox.addWidget(self.table)
        self.setLayout(self.vBox)

    def table_loader(self, results: []):
        try:
            self.table.load_data(results)
        except TypeError:
            pass


if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    mainBase = DummyView()
    mainBase.show()
    # directory.show()
    sys.exit(qApp.exec_())

