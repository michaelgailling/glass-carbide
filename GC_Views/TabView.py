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
from PySide2.QtWidgets import QTabWidget, QFrame, QVBoxLayout, QMessageBox

from GC_Components.MainComponents import MainNavButtons
from GC_Views.DummyView import DummyView
from TableView import TableView
from HomeView import HomeView
from ResultsOutputView import ResultsOutputView
from GC_Services.FileIo import FileIo


class TabView(QFrame):
    def __init__(self, parent=None, file_io=FileIo()):
        super(TabView, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self.fio = file_io
        self.dir = ""

        # Views for tabs
        self.homeView = HomeView(self, self.fio)
        self.tableView = TableView(self, self.fio)
        self.resultsView = ResultsOutputView(self, self.fio)

        # Tab Widget
        self.tabWidget = QTabWidget(self)
        self.tabWidget.setStyleSheet("QTabBar::tab { height: 25%; width: 244%;\n"
                                     "border: 2px solid rgb(0, 0, 205); background-color: rgb(255, 255, 255);\n"
                                     "color: rgb(0, 0, 205); border-bottom:none; margin-left: 2px;}")

        # Setting views in tabs
        self.set_tab_frame(self.homeView, 0)
        self.set_tab_frame(self.tableView, 1)
        self.set_tab_frame(self.resultsView, 2)

        # Tab Index Variable
        self.tabIndex = 0
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget.setTabEnabled(0, True)
        self.tabWidget.setTabEnabled(1, False)
        self.tabWidget.setTabEnabled(2, False)

        # Setup Nav Buttons
        self.main_nav = MainNavButtons()
        self.main_nav.continueBtn.clicked.connect(self.continue_clicked)
        self.main_nav.backBtn.clicked.connect(self.back_clicked)

        self.layout.addWidget(self.tabWidget)
        self.layout.addWidget(self.main_nav)
        self.setLayout(self.layout)
        self.setGeometry(0, 0, 900, 600)

    def set_tab_frame(self, frame: QFrame, index_num: int):
        self.tabWidget.insertTab(index_num, frame, f"Step {index_num + 1}")

    def tab_index_setter(self, index_num=0):
        self.tabWidget.setCurrentIndex(index_num)
        self.tabWidget.setTabEnabled(self.tabIndex, False)
        self.tabIndex = index_num
        self.tabWidget.setTabEnabled(self.tabIndex, True)

    def tab_index_getter(self):
        return self.tabIndex

    def dir_getter(self):
        self.dir = self.fio.project_dir
        self.tableView.lfi_file_select.set_input_text(self.dir)

    def get_selection(self):
        selection = self.tableView.create_selection()
        self.resultsView.data = selection

    def continue_clicked(self):
        if self.homeView.mappingView.get_dir_path():
            self.dir_getter()

        if self.tab_index == 0:
            self.tab_index_setter(1)
        elif self.tab_index == 1:
            results = self.tableView.create_selection()
            self.tab_index_setter(2)
            self.resultsView.load_table_data(results)
        elif self.tab_index == 2:
            msg = QMessageBox()
            msg.setWindowTitle("Are you sure?")
            msg.setText("Open { Project Name } in { Software }?")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.exec_()

    def back_clicked(self):
        if self.tab_index == 0:
            msg = QMessageBox()
            msg.setWindowTitle("Save your progress?")
            msg.setText("Would you like to save your progress?")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Save | QMessageBox.Cancel | QMessageBox.Close)
            msg.exec_()
        elif self.tab_index == 1:
            self.tab_index_setter(0)
        elif self.tab_index == 2:
            self.tab_index_setter(1)
