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
    """Tab View

                    Summary:
                        A class for {Type} that includes:

                        -{Description} to the {Location eg left}

                    Attributes:
                        label, {AttributeName}

                    Methods:
                        get_input_text, {MethodName}

                    Attributes
                    ----------
                        label : QLabel
                            Text Label for Input Box
                        {AttributeName} : {AttributeClass}
                            {Property} for {Type}

                    Methods
                    -------
                        get_input_text(self)
                            Return the text in the input box
                        {MethodName}({Parameters})
                            {Functionality}
                """
    def __init__(self, parent=None, file_io=FileIo()):
        """Constructor:
                                    Initialize Image Preview View

                                    Parameters:
                                        self
                                        parent : QFrame
                                        file_io : FileIo
                                            {Description}
                                    Returns:
                                        None
                                """
        # -------------------------------------------init Start-------------------------------------------
        super(TabView, self).__init__(parent)
        self.fio = file_io
        self.dir = ""

        # Views for tabs
        self.hv_homeView = HomeView(self, self.fio)
        self.tv_tableView = TableView(self, self.fio)
        self.rv_resultsView = ResultsOutputView(self, self.fio)

        # ----------------------------------------------
        # -----------------tw_tabWidget-----------------
        # ----------------------------------------------

        self.tw_tabWidget = QTabWidget(self)
        self.tw_tabWidget.setStyleSheet("QTabBar::tab {font:Verdana;height:55%;border:3px solid #1000A0;width:390%;"
                                     "background-color:white;color:#1000A0; border-bottom:2px dashed #1000A0;padding:0;"
                                     "font-weight:600;font-size:13px;margin:0 auto -10 auto;border-radius:13px;}"
                                     "QTabBar::tab:selected{background-color:#1000A0;color:white;}")

        # Setting views in tabs
        self.set_tab_frame(self.hv_homeView, 0)
        self.set_tab_frame(self.tv_tableView, 1)
        self.set_tab_frame(self.rv_resultsView, 2)

        # Tab Index Variable
        self.tabIndex = 0
        self.tw_tabWidget.setCurrentIndex(0)
        self.tw_tabWidget.setTabEnabled(0, True)
        self.tw_tabWidget.setTabEnabled(1, False)
        self.tw_tabWidget.setTabEnabled(2, False)

        # ----------------------------------------------
        # -----------------mnb_main_nav-----------------
        # ----------------------------------------------

        self.mnb_main_nav = MainNavButtons()
        self.mnb_main_nav.continueBtn.clicked.connect(self.continue_clicked)
        self.mnb_main_nav.backBtn.clicked.connect(self.back_clicked)

        # -------------------------------------------------
        # -----------------vbl_main_layout-----------------
        # -------------------------------------------------

        self.vbl_main_layout = QVBoxLayout(self)

        self.vbl_main_layout.addWidget(self.tw_tabWidget)
        self.vbl_main_layout.addWidget(self.mnb_main_nav)
        self.setLayout(self.vbl_main_layout)
        self.setStyleSheet('TableView{border:3px solid #1000A0;margin:0;} '
                           'ResultsOutputView{border:3px solid #1000A0;margin:0}')

        # -------------------------------------------init End-------------------------------------------

    def set_tab_frame(self, frame: QFrame, index_num: int):
        if index_num == 0:
            msg = "Select Folder Directories for Project Mapping"
        elif index_num == 1:
            msg = "Load CSV and Select Assets"
        elif index_num == 2:
            msg = "Preview"
        self.tw_tabWidget.insertTab(index_num, frame, f"Step {index_num + 1} - {msg}")

    def tab_index_setter(self, index_num=0):
        self.tw_tabWidget.setCurrentIndex(index_num)
        self.tw_tabWidget.setTabEnabled(self.tabIndex, False)
        self.tabIndex = index_num
        self.tw_tabWidget.setTabEnabled(self.tabIndex, True)

    def tab_index_getter(self):
        return self.tabIndex

    def get_selection(self):
        selection = self.tv_tableView.create_selection()
        self.rv_resultsView.data = selection

    def continue_clicked(self):
        if self.hv_homeView.dmv_mapping_view.get_dir_path():
            self.dir = self.fio.project_dir
            self.tv_tableView.lfi_file_select.set_input_text(self.dir)

        if self.tabIndex == 0:
            self.tab_index_setter(1)
        elif self.tabIndex == 1:
            results = self.tv_tableView.create_selection()
            self.tab_index_setter(2)
            self.rv_resultsView.load_table_data(results)
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
