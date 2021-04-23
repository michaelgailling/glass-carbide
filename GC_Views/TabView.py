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
        self.set_tab_frame(self.homeView, 0)
        self.set_tab_frame(self.tableView, 1)
        self.set_tab_frame(self.previewView, 2)

        self.layout.addWidget(self.tabWidget)
        self.setLayout(self.layout)
        self.setGeometry(0, 0, 800, 400)

    def set_tab_frame(self, frame: QFrame, index_num: int):
        self.tabWidget.insertTab(index_num, frame, f"Step {index_num + 1}")
        self.tabWidget.setCurrentIndex(0)

    def dir_getter(self):
        self.dir = self.homeView.mappingView.get_dir_path()
        self.tableView.lfi_file_select.set_input_text(self.dir)
