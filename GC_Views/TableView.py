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
from PySide2.QtWidgets import QApplication, QFrame, QPushButton, QVBoxLayout, QTableWidgetItem, QCheckBox, QComboBox

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
        self.lfi_file_select = LabeledFileInput(self, label_text="Select CSV", file_type="CSV Format (*.csv)")

        # Load Button
        self.btn_load_file = QPushButton("Load File")
        self.btn_load_file.clicked.connect(self.load_file)

        # Layout loading
        self.vBox.addWidget(self.dt_table)
        self.vBox.addWidget(self.lfi_file_select)
        self.vBox.addWidget(self.btn_load_file)
        self.setLayout(self.vBox)
 
        self.setGeometry(0, 0, 800, 500)

    def load_file(self):
        self.csv_handler.data.clear()
        input_path = self.lfi_file_select.get_input_text()

        if input_path:
            self.csv_handler.import_data(input_path)

            csv_headers = []
            csv_data = []
            csv_headers = self.csv_handler.data.pop(0)
            csv_headers.insert(0, "Select")
            csv_data = self.csv_handler.data

            width = len(csv_data[0])
            height = len(csv_data)

            self.dt_table.set_dimensions(width, height)

            self.dt_table.load_data(csv_data)

            combobox = QComboBox()
            combobox.addItems(["None", "File Name", "Asset Path"])
            self.dt_table.insert_control_row("combobox", 0)

            self.dt_table.insert_control_column("checkbox", 1)

            self.dt_table.set_headers(csv_headers)
            # for x in range(width+1):
            #     combobox = QComboBox(self)
            #     combobox.addItems(["None", "File Name", "Asset Path"])
            #     self.dt_table.set_cell_widget(combobox, x+1, 0)

            # for y in range(height+1):
            #     checkbox = QCheckBox(self)
            #     self.dt_table.set_cell_widget(checkbox, 0, y+1)




if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    tab = TableView()
    tab.show()
    sys.exit(qApp.exec_())

