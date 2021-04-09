# LOBI
# Land of Bad Ideas
# Use this file for experimentation only,
# Never directly import or reference this file
from PySide2.QtWidgets import QApplication, QWidget, QHBoxLayout, QMainWindow, QAction, QFrame, QPlainTextEdit, \
    QSplitter, QVBoxLayout, QFileDialog, QTableWidget, QTableWidgetItem, QTableView, QLabel, QPushButton


derp = None
herp = ""

if 0 or herp:
    print("DERP")
else:
    print("NOT DERP")


class Map_Panel(QWidget):
    def __init__(self, parent=None):
        super(Map_Panel, self).__init__(parent)
        self.panel_window = QHBoxLayout()

    def return_hbox(self):
        btn = QPushButton('TEST', self)
        self.panel_window.addWidget(btn)
        return self.panel_window
