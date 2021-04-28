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

from PySide2.QtWidgets import QApplication, QFrame, QPushButton, QVBoxLayout, QTableWidgetItem, QHBoxLayout, QComboBox

from GC_Components.InputComponents import LabeledFileInput
from GC_Components.TableComponents import DataTable
from GC_Services.csvIO import CsvIo


class TableView(QFrame):
    def __init__(self, parent=None):
        super(TableView, self).__init__(parent)
        self.vBox = QVBoxLayout()
        self.csv_handler = CsvIo()

        # Table
        self.dt_table = DataTable(self)
        self.column_definitions = []

        # Labeled File Input
        self.lfi_file_select = LabeledFileInput(self, label_text="Select Episode CSV", file_type="CSV Format (*.csv)")

        # Load Button
        self.btn_load_file = QPushButton("Load To Table")
        # self.btn_load_file.setStyleSheet("background-color:blue;color:white;padding:10;border : 2px solid blue;"
        #                                  "border-radius:20px")
        self.btn_load_file.clicked.connect(self.load_file)

        self.btn_test = QPushButton("TEST")

        self.btn_test.clicked.connect(self.create_selection)

        # Layout loading
        self.vBox.addWidget(self.dt_table)
        self.vBox.addWidget(self.lfi_file_select)
        self.vBox.addWidget(self.btn_load_file)
        self.vBox.addWidget(self.btn_test)
        self.setLayout(self.vBox)
 
        self.setGeometry(0, 0, 800, 500)

    def load_file(self):
        self.csv_handler.data.clear()
        input_path = self.lfi_file_select.get_input_text()

        if input_path:
            self.csv_handler.import_data(input_path)

            csv_headers = self.csv_handler.data[0]
            csv_headers.insert(0, "Select")
            csv_data = self.csv_handler.data[1:]

            self.dt_table.clear_table()

            self.dt_table.load_data(csv_data)

            combo_options = ["None",
                             "Asset Name(s)",
                             "ShotCode",
                             "Duration",
                             "Frames", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
                             "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]

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

        width = len(current_table[0])
        height = len(current_table)

        mapped_columns = self.dt_table.mappings
        selected_rows = self.dt_table.selections
        selected_data = []

        for i in range(len(selected_rows)):
            if selected_rows[i]:
                selected_data.append(current_table[i])

        if selected_data:
            selected_data.insert(0, self.csv_handler.data[0])
            selected_data[0].pop(0)
            selected_data.insert(1, mapped_columns)

        return selected_data


if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    tab = TableView()
    tab.show()
    sys.exit(qApp.exec_())

