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
from PySide2.QtWidgets import QApplication, QFrame, QPushButton, QVBoxLayout, QMessageBox, QCheckBox
from GC_Services.FileIo import FileIo
from GC_Components.InputComponents import LabeledFileInput
from GC_Components.TableComponents import DataTable
from GC_Services.csvIO import CsvIo


class GCTableView(QFrame):
    """Table View

        Summary:
            A class for load & display of CSV on Data Table that includes:

            -Data Table of CSV on top
            -LabeledFileInput for CSV selection and Load button on bottom


        Attributes:
            csv_handler, fio, column_definitions, dt_table, lfi_file_select, btn_load_file, vbl_main_layout

        Methods:
            load_file, create_selection

        Attributes
        ----------
            csv_handler : CsvIo
                CsvIo handles load, parse and display of csv files
            fio : file_io
                File input & output
            column_definitions : []
                Array for column definitions of dt_table Data Table
            dt_table : DataTable
                Data table for csv
            lfi_file_select : LabeledFileInput
                LabeledFileInput for open file dialogue to select csv file
            btn_load_file : QPushButton
                Button to load selected csv to dt_table Data Table
            vbl_main_layout : QVBoxLayout
                Main Vertical Layout

        Methods
        -------
            load_file(self)
                Loads CSV to table
            create_selection(self)
                Returns selected data from table
    """
    def __init__(self, parent=None, file_io=FileIo()):
        """Constructor:
            Initialize Table View

            Parameters:
                self
                parent : QFrame
                file_io : FileIo
                    {Description}
            Returns:
                None
        """
        # -------------------------------------------init Start-------------------------------------------
        super(GCTableView, self).__init__(parent)
        self.csv_handler = CsvIo()
        self.fio = file_io
        self.column_definitions = []

        # ----------------------------------------------
        # -----------------dt_table---------------------
        # ----------------------------------------------
        self.dt_table = DataTable(self)

        # ----------------------------------------------
        # -----------------lfi_file_select--------------
        # ----------------------------------------------
        self.lfi_file_select = LabeledFileInput(self, label_text="Select CSV", file_type="CSV Format (*.csv)")

        # ----------------------------------------------
        # -----------------btn_load_file----------------
        # ----------------------------------------------
        self.btn_load_file = QPushButton("Load To Table")
        self.btn_load_file.clicked.connect(self.load_file)

        # ----------------------------------------------
        # -----------------vbl_main_layout--------------
        # ----------------------------------------------

        self.vbl_main_layout = QVBoxLayout()

        self.vbl_main_layout.addWidget(self.dt_table)
        self.vbl_main_layout.addWidget(self.lfi_file_select)
        self.vbl_main_layout.addWidget(self.btn_load_file, alignment=Qt.AlignHCenter)
        self.setLayout(self.vbl_main_layout)

        self.setGeometry(0, 0, 800, 600)
        self.setStyleSheet('QFrame DataTable{border:1px solid #1000A0;background-color:#e6e6e6;}'
                           'QCheckBox{width:90%;margin: 0 auto;} QTableWidget{font-weight:600}')

        # -------------------------------------------init End-------------------------------------------

    def load_file(self):
        self.csv_handler.data.clear()
        input_path = self.lfi_file_select.get_input_text()

        if input_path:
            self.csv_handler.import_data(input_path)

            csv_headers = self.csv_handler.data[0]
            csv_headers.insert(0, "Select")
            csv_data = self.csv_handler.data[1:]

            for item in csv_data:
                item.insert(0, False)

            self.dt_table.load_table(csv_data)

            combo_options = ["None",
                             "Assets",
                             "ShotCode",
                             "Duration",
                             "Frames",
                             "Resolution",
                             ""]
            combo_row = [False]
            for i in range(self.dt_table.width - 1):
                combo_row.append(combo_options)

            self.dt_table.insert_row(combo_row)

            self.dt_table.table.cellWidget(0, 0).clicked.connect(self.select_all)

            self.dt_table.set_headers(csv_headers)

        else:
            msg_warning = QMessageBox()
            msg_warning.setIcon(QMessageBox.Warning)
            msg_warning.setWindowTitle("Before Loading")
            msg_warning.setText("Select CSV to Load")
            msg_warning.exec_()

    def select_all(self):
        test = QCheckBox()

        is_checked = self.dt_table.table.cellWidget(0, 0).isChecked()

        if(is_checked):
            for y in range(self.dt_table.height):
                self.dt_table.table.cellWidget(y, 0).setChecked(True)
        else:
            for y in range(self.dt_table.height):
                self.dt_table.table.cellWidget(y, 0).setChecked(False)

        self.get_all_selected()

    def get_all_selected(self):
        all_rows = self.dt_table.get_all_rows()
        combos = all_rows.pop(0)[1:]
        selected_rows = [combos]

        for i in range(0, len(all_rows)):
            row = all_rows[i]
            row_selected = row[0]
            if row_selected:
                selected_rows.append(row[1:])

        for x in range(len(combos)-1, -1, -1):
            header = selected_rows[0][x]
            if header == "None":
                for y in range(len(selected_rows)):
                    del selected_rows[y][x]

        return selected_rows






    def create_selection(self):
        width = self.dt_table.width
        height = self.dt_table.height

        current_table = []

        for y in range(0, height):
            row = []
            for x in range(1, width):
                row.append(self.dt_table.get_cell_text(x, y))
            current_table.append(row)

        mapped_columns = []
        selected_data = []

        for i in range(width - 1):
            mapping_text = self.dt_table.mappings[i].currentText()
            if mapping_text != "None" and mapping_text != "":
                mapped_columns.append(mapping_text)

        for y in range(height - 1):

            if self.dt_table.selections[y].isChecked():
                row = []
                for x in range(width-1):
                    mapping_text = self.dt_table.mappings[x].currentText()
                    if mapping_text != "None" and mapping_text != "":
                        row.append(current_table[y][x])

                selected_data.append(row)

        if selected_data:
            selected_data.insert(0, mapped_columns)

        return selected_data


if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    tab = GCTableView()
    tab.show()
    sys.exit(qApp.exec_())

