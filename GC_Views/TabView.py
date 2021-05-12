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

from PySide2.QtWidgets import QTabWidget, QFrame, QVBoxLayout, QMessageBox
from GC_Components.MainComponents import MainNavButtons
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
        self.tabWidget.setStyleSheet("QTabBar::tab {font:Verdana;height:55%;border:3px solid #1000A0;width:390%;"
                                     "background-color:white;color:#1000A0; border-bottom:2px dashed #1000A0;padding:0;"
                                     "font-weight:600;font-size:13px;margin:0 auto -10 auto;border-radius:13px;}"
                                     "QTabBar::tab:selected{background-color:#1000A0;color:white;}")

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
        self.setStyleSheet('TableView{border:3px solid #1000A0;margin:0;} '
                           'ResultsOutputView{border:3px solid #1000A0;margin:0}')

    def set_tab_frame(self, frame: QFrame, index_num: int):
        if index_num == 0:
            msg = "Select Folder Directories for Project Mapping"
        elif index_num == 1:
            msg = "Load CSV and Select Assets"
        elif index_num == 2:
            msg = "Preview"
        self.tabWidget.insertTab(index_num, frame, f"Step {index_num + 1} - {msg}")

    def tab_index_setter(self, index_num=0):
        self.tabWidget.setCurrentIndex(index_num)
        self.tabWidget.setTabEnabled(self.tabIndex, False)
        self.tabIndex = index_num
        self.tabWidget.setTabEnabled(self.tabIndex, True)

    def tab_index_getter(self):
        return self.tabIndex

    def get_selection(self):
        selection = self.tableView.create_selection()
        self.resultsView.data = selection

    def continue_clicked(self):
        if self.homeView.dmv_mapping_view.get_dir_path():
            self.dir = self.fio.project_dir
            self.tableView.lfi_file_select.set_input_text(self.dir)

        if self.tabIndex == 0:
            self.tab_index_setter(1)
        elif self.tabIndex == 1:
            results = self.tableView.create_selection()
            self.tab_index_setter(2)
            self.resultsView.load_table_data(results)
        elif self.tabIndex == 2:
            msg = QMessageBox()
            msg.setWindowTitle("Are you sure?")
            msg.setText("Open { Project Name } in { Software }?")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.exec_()

    def back_clicked(self):
        if self.tabIndex == 0:
            pass
        elif self.tabIndex == 1:
            self.tab_index_setter(0)
        elif self.tabIndex == 2:
            self.tab_index_setter(1)
