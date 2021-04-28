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
from PySide2.QtCore import QEvent
from PySide2.QtWidgets import QTabWidget, QFrame, QVBoxLayout
from TableView import TableView
from HomeView import HomeView
from ResultsOutputView import ResultsOutputView


class TabView(QFrame):
    def __init__(self, parent=None):
        super(TabView, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        self.dir = ""

        # Views for tabs
        self.homeView = HomeView()
        self.tableView = TableView()
        self.previewView = ResultsOutputView()

        # Tab Widget
        self.tabWidget = QTabWidget(self)
        self.tabWidget.setStyleSheet("QTabBar::tab { height: 25%; width: 244%;\n"
                                     "border: 2px solid rgb(0, 0, 205); background-color: rgb(255, 255, 255);\n"
                                     "color: rgb(0, 0, 205); border-bottom:none; margin-left: 2px;}")

        # Setting views in tabs
        self.set_tab_frame(self.homeView, self.homeView.tabIndex)
        self.set_tab_frame(self.tableView, self.tableView.tabIndex)
        self.set_tab_frame(self.previewView, self.previewView.tabIndex)

        # Setting tabs be non selectable
        self.tabWidget.setEnabled(False)

        self.layout.addWidget(self.tabWidget)
        self.setLayout(self.layout)
        self.setGeometry(0, 0, 800, 400)

        # Tab Index Variable
        self.tabWidget.setCurrentIndex(0)
        self.tabIndex = 0

    def set_tab_frame(self, frame: QFrame, index_num: int):
        self.tabWidget.insertTab(index_num, frame, f"Step {index_num + 1}")
        self.tabWidget.setCurrentIndex(0)

    def tab_index_setter(self, index_num: int):
        self.tabWidget.setCurrentIndex(index_num)
        self.tabIndex = index_num

    def tab_index_getter(self):
        return self.tabIndex

    def dir_getter(self):
        self.dir = self.homeView.mappingView.get_dir_path()
        self.tableView.lfi_file_select.set_input_text(self.dir)
