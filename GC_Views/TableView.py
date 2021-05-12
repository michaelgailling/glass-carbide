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
from PySide2.QtWidgets import QApplication, QFrame, QPushButton, QVBoxLayout, QTableWidgetItem, QHBoxLayout, QComboBox
from GC_Services.FileIo import FileIo
from GC_Components.InputComponents import LabeledFileInput
from GC_Components.TableComponents import DataTable
from GC_Services.csvIO import CsvIo


class TableView(QFrame):
    def __init__(self, parent=None, file_io=FileIo()):
        # -------------------------------------------init Start-------------------------------------------
        super(TableView, self).__init__(parent)
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
        self.btn_load_file.setStyleSheet("background-color:#1000A0;color:white;padding:13 3;border:2px solid #1000A0;"
                                         "border-radius:10px;font-weight:600;")

        # ----------------------------------------------
        # -----------------vbl_main_layout--------------
        # ----------------------------------------------

        self.vbl_main_layout = QVBoxLayout()

        self.vbl_main_layout.addWidget(self.dt_table)
        self.vbl_main_layout.addWidget(self.lfi_file_select)
        self.vbl_main_layout.addWidget(self.btn_load_file, alignment=Qt.AlignHCenter)
        self.setLayout(self.vbl_main_layout)

        self.setGeometry(0, 0, 800, 600)
        self.setStyleSheet('QFrame{font-weight:600;} QLineEdit{border:2px solid #1000A0}'
                           'QFrame DataTable{border:1px solid #1000A0;background-color:#e6e6e6}')

        # -------------------------------------------init End-------------------------------------------

    def load_file(self):
        self.csv_handler.data.clear()
        input_path = self.lfi_file_select.get_input_text()

        if input_path:
            self.csv_handler.import_data(input_path)

            csv_headers = self.csv_handler.data[0]
            csv_headers.insert(0, "Select")
            csv_data = self.csv_handler.data[1:]

            self.dt_table.clear_table()

            self.dt_table.load_table(csv_data)

            combo_options = ["None",
                             "Assets",
                             "ShotCode",
                             "Duration",
                             "Frames",
                             "Resolution",
                             ""]

            self.dt_table.insert_control_row("combobox", 0, combo_options)

            self.dt_table.insert_control_column("checkbox", 1)

            self.dt_table.set_headers(csv_headers)

    def create_selection(self):
        width = self.dt_table.width
        height = self.dt_table.height

        current_table = []

        for y in range(1, height):
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
    tab = TableView()
    tab.show()
    sys.exit(qApp.exec_())

