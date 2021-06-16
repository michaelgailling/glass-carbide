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

import asyncio
import inspect
import sys
from PySide2.QtGui import QColor, Qt, QBrush
from PySide2.QtWidgets import QFrame, QTableWidget, QVBoxLayout, QTableWidgetItem, QApplication, QWidget, QComboBox, \
    QCheckBox, QHeaderView

#
# class DataTable(QFrame):
#     """Data Table
#
#         Summary:
#             A class for a data table that includes:
#
#             -Method for altering cell bg color
#
#             -Method for altering cell text color
#
#             -Method for setting and getting cell values
#
#         Attributes:
#             vbox, mappings, selections, readonly, table, width, height
#
#         Methods:
#             clear_table, set_dimensions, set_headers, style_headers, insert_control_row, insert_control_column,
#             insert_data_column, create_control_widget, load_table, fit_headers_to_content, cell_changed,
#             set_cell_tooltip, set_cell_color, set_text_color, set_cell_widget, set_cell_text, get_cell_text
#
#         Attributes
#         ----------
#             vbox : QVBoxLayout
#                 Vertical Layout
#             mappings : []
#                 !!! Array of mappings of !!!
#             selections : []
#                 Array of selected rows and columns
#             readonly : bool
#                 Variable for whether cell is editable or readonly
#             table : QTableWidget
#                 Table to which data is loaded
#             width : int
#                 Width of table
#             height : int
#                 Height of table
#
#         Methods
#         -------
#             clear_table(self)
#                 Clears table contents
#             set_dimensions(self, width=0, height=0)
#                 Sets number of columns and rows in table
#             set_headers(self, headers)
#                 Sets table headers
#             style_headers(self)
#                 Sets styling for headers
#             insert_control_row(self, widget_type=None, start_index=0, options=[])
#                 Inserts control row in table
#             insert_control_column(self, widget_type=None, start_index=0, options=[])
#                 Inserts control column in table
#             insert_data_column(self, header="", start_index_y=0, insert_before=True, data=[])
#                 Inserts data by column
#             create_control_widget(self, widget_type=None, options=[])
#                 Inserts combo boxes if control row or check boxes if control column
#             load_table(self, data=[])
#                 Loads data to table
#             fit_headers_to_content(self)
#                 Sets header width to fit widest column
#             cell_changed(self, y, x)
#                 Slot for cell changed signal
#             set_cell_tooltip(self, x=0, y=0, tooltip_text="")
#                 Set tooltip for cell
#             set_cell_color(self, x=0, y=0, color="white")
#                 Sets the background color of the specified cell
#             set_text_color(self, x=0, y=0, color="black")
#                 Sets the text color of the specified cell
#             set_cell_widget(self,  widget=None, x=0, y=0,)
#                 Sets the cell's widget
#             set_cell_text(self, x=0, y=0, text="")
#                 Sets the text of the specified cell
#             get_cell_text(self, x=0, y=0)
#                 Gets the text of the specified cell
#     """
#
#     def __init__(self, parent=None, width=0, height=0, readonly=False, log_data=False):
#         """
#         Constructs all the necessary attributes for the Data Table object.
#
#         Parameters
#         ----------
#             self
#             parent : QFrame
#             width : int
#                 The number of columns
#             height : int
#                 The number of rows
#             readonly : bool
#                 Set readonly status
#             log_data : bool
#                 Set log recording status
#         """
#         super(DataTable, self).__init__(parent)
#
#         self.headers =[]
#
#         self.mappings = []
#         self.selections = []
#         self.readonly = readonly
#
#         self.table = QTableWidget()
#         self.width = width
#         self.height = height
#         self.set_dimensions(width, height)
#
#         if log_data:
#             self.table.cellChanged.connect(self.cell_changed)
#         self.table.verticalHeader().hide()
#
#         self.vbox = QVBoxLayout()
#         self.vbox.addWidget(self.table)
#
#         self.setLayout(self.vbox)
#
#     def clear_table(self):
#         self.table.clear()
#
#     def set_dimensions(self, width=0, height=0):
#         self.width = width
#         self.height = height
#         self.table.setColumnCount(width)
#         self.table.setRowCount(height)
#
#     def get_dimensions(self):
#         return {"x": self.width, "y": self.height}
#
#     def set_headers(self, headers):
#         self.headers = headers
#         self.table.setHorizontalHeaderLabels(headers)
#         self.table.horizontalHeader().setStyleSheet('color:#1000A0')
#         self.style_headers()
#
#     def get_headers(self):
#         return self.headers
#
#     def style_headers(self):
#         self.table.horizontalHeader().setStyleSheet("::section{background-color:#1000A0;color:white;font-weight:bold}")
#         self.table.horizontalHeader().setAutoFillBackground(True)
#
#     def insert_row(self):
#         pass
#
#     def add_row(self):
#         pass
#
#     def insert_control_row(self, widget_type=None, start_index=0, options=[]):
#         self.table.insertRow(0)
#
#         self.height += 1
#
#         if widget_type:
#             width = self.width
#             self.mappings = []
#             for x in range(start_index, width):
#                 self.mappings.append(self.create_control_widget(widget_type, options))
#                 self.set_cell_widget(self.mappings[-1], x, 0)
#
#     def insert_control_column(self, widget_type=None, start_index=0, options=[]):
#         self.table.insertColumn(0)
#
#         self.width += 1
#
#         if widget_type:
#             height = self.height
#             self.selections = []
#             for y in range(start_index, height):
#                 self.selections.append(self.create_control_widget(widget_type, options))
#                 self.set_cell_widget(self.selections[-1], 0, y)
#
#     def insert_data_column(self, header="", start_index_y=0, insert_before=True, data=[]):
#         header_item = QTableWidgetItem(header)
#         if insert_before:
#             self.table.insertColumn(0)
#             self.table.setHorizontalHeaderItem(0, header_item)
#             for y in range(start_index_y, len(data)):
#                 cell = QTableWidgetItem(data[y])
#                 self.table.setItem(y, 0, cell)
#         else:
#             self.table.insertColumn(self.width)
#             self.table.setHorizontalHeaderItem(self.width, header_item)
#             for y in range(start_index_y, len(data)):
#                 cell = QTableWidgetItem(data[y])
#                 self.table.setItem(y, self.width, cell)
#         self.width += 1
#
#     def create_control_widget(self, widget_type=None, options=[]):
#         if widget_type == "combobox":
#             widget = QComboBox()
#
#             widget.setEditable(True)
#
#             if options:
#                 widget.addItems(options)
#
#         elif widget_type == "checkbox":
#             widget = QCheckBox(self)
#
#         return widget
#
#     def load_table(self, data=[]):
#
#         data_type = type(data[0])
#         if data_type is str:
#             height = len(data)
#
#             self.set_dimensions(1, height)
#
#             for y in range(height):
#                 cell = QTableWidgetItem(data[y])
#                 if self.readonly:
#                     cell.setFlags(Qt.ItemIsEditable)
#                 self.table.setItem(y, 0, cell)
#
#             asyncio.run(self.fit_headers_to_content())
#         else:
#             height = len(data)
#             width = len(data[0])
#             self.set_dimensions(width, height)
#
#             for y in range(height):
#                 for x in range(width):
#                     cell = QTableWidgetItem(data[y][x])
#                     if self.readonly:
#                         cell.setFlags(Qt.ItemIsEditable)
#                     self.table.setItem(y, x, cell)
#
#         # asyncio.run(self.fit_headers_to_content())
#
#     def get_table_data(self):
#         table_data = []
#
#         for y in range(self.height):
#             table_row = []
#
#             for x in range(self.width):
#                 table_row.append(self.get_cell_text(x, y))
#
#             table_data.append(table_row)
#
#         return table_data
#
#     async def fit_headers_to_content(self):
#         header = self.table.horizontalHeader()
#         width = self.table.columnCount()
#         for i in range(width):
#             header.setSectionResizeMode(i, QHeaderView.ResizeToContents)
#
#     def cell_changed(self, y=0, x=0):
#         """
#         Slot for handling cell change events
#
#         Parameters
#         ----------
#         x : int
#             Cell X co-ordinate
#         y: int
#             Cell Y co-ordinate
#
#         Returns
#         -------
#         None
#         """
#         asyncio.run(self.log_cell(x, y))
#
#     def set_cell_tooltip(self, x=0, y=0, tooltip_text=""):
#         self.table.item(y, x).setToolTip(tooltip_text)
#
#     def set_cell_color(self, x=0, y=0, color="white"):
#         """
#         Method for setting the bg color of a cell
#
#         Parameters
#         ----------
#         x : int
#             Cell X co-ordinate
#         y: int
#             Cell Y co-ordinate
#         color : string
#             Color as to set cell background color
#
#         Returns
#         -------
#         None
#         """
#         self.table.item(y, x).setBackgroundColor(QColor(color))
#
#     def set_text_color(self, x=0, y=0, color="black"):
#         """
#         Method for setting the text color of a cell
#
#         Parameters
#         ----------
#         x : int
#             Cell X co-ordinate
#         y: int
#             Cell Y co-ordinate
#         color : string
#             Color to set cell text color
#
#         Returns
#         -------
#         None
#         """
#         self.table.item(y, x).setTextColor(QColor(color))
#
#     def set_cell_widget(self,  widget=None, x=0, y=0,):
#         self.table.setCellWidget(y, x, widget)
#
#     def set_cell_text(self, x=0, y=0, text=""):
#         """
#         Method for setting the text content of a cell
#
#         Parameters
#         ----------
#         x : int
#             Cell X co-ordinate
#         y: int
#             Cell Y co-ordinate
#         text : string
#             Text to set cell content
#
#         Returns
#         -------
#         None
#         """
#         cell = QTableWidgetItem(text)
#         self.table.setItem(y, x, cell)
#
#     def get_cell_text(self, x=0, y=0):
#         """
#         Method for Getting the text content of a cell
#
#         Parameters
#         ----------
#         x : int
#             Cell X co-ordinate
#         y: int
#             Cell Y co-ordinate
#
#         Returns
#         -------
#         text_content : string
#             Text content of specified cell
#         """
#         text_content = self.table.item(y, x).text()
#         return text_content
#
#     async def log_cell(self, x=0, y=0):
#         """
#         Method for logging the current state of a cell to console
#
#         Parameters
#         ----------
#         x : int
#             Cell X co-ordinate
#         y: int
#             Cell Y co-ordinate
#
#         Returns
#         -------
#         None
#         """
#         cell_text = self.get_cell_text(x, y)
#         bg_color_red = str(self.table.item(y, x).backgroundColor().red())
#         bg_color_green = str(self.table.item(y, x).backgroundColor().green())
#         bg_color_blue = str(self.table.item(y, x).backgroundColor().blue())
#         bg_color_alpha = str(self.table.item(y, x).backgroundColor().alpha())
#         text_color_red = str(self.table.item(y, x).textColor().red())
#         text_color_green = str(self.table.item(y, x).textColor().green())
#         text_color_blue = str(self.table.item(y, x).textColor().blue())
#         text_color_alpha = str(self.table.item(y, x).textColor().alpha())
#
#         print()
#         print()
#
#         print("Cell Changed")
#         print("-------------------------------------")
#         print("x:" + str(x) + " y:" + str(y))
#         print()
#
#         print("Cell Data")
#         print("-------------------------------------")
#         print(cell_text)
#         print()
#
#         print("Background Color")
#         print("-------------------------------------")
#         print("RED: " + bg_color_red + " GREEN: " + bg_color_green + " BLUE: " + bg_color_blue +
#               " ALPHA: " + bg_color_alpha)
#         print()
#
#         print("Text Color")
#         print("-------------------------------------")
#         print("RED: " + text_color_red + " GREEN: " + text_color_green + " BLUE: " + text_color_blue +
#               " ALPHA: " + text_color_alpha)
#
#         print()
#         print()

#
# class SimpleDataTable(DataTable):
#     """Asset Data Table
#
#         Summary:
#             A class for loading assets in a data table
#
#         Attributes:
#             mappings, data, readonly
#
#         Methods:
#             load_table
#
#         Attributes
#         ----------
#             mappings : []
#                 !!! Array of mappings of !!!
#             data : []
#                 Array of data from selected column
#             readonly : bool
#                 Variable for whether cell is editable or readonly
#
#         Methods
#         -------
#             load_table(self, data=[])
#                 Loads passed in array of assets in DataTable
#     """
#
#     def __init__(self,  parent=None, width=0, height=0, readonly=False, log_data=False):
#         """
#             Constructs all the necessary attributes for the AssetDataTable object.
#
#             Parameters
#             ----------
#                 self
#                 parent : DataTable
#                 width : int
#                     The number of columns
#                 height : int
#                     The number of rows
#                 readonly : bool
#                     Set readonly status
#                 log_data : bool
#                     Set log recording status
#         """
#         super(SimpleDataTable, self).__init__(parent)
#         self.readonly = readonly
#         self.data = []
#         self.mappings = []
#
#     def load_table(self, data=[]):
#         height = len(data)
#
#         self.set_dimensions(1, height)
#
#         for y in range(height):
#             cell = QTableWidgetItem(data[y])
#             if self.readonly:
#                 cell.setFlags(Qt.ItemIsEditable)
#             self.table.setItem(y, 0, cell)
#
#         asyncio.run(self.fit_headers_to_content())



class DataTable(QFrame):

    def __init__(self, parent=None, width=0, height=0, readonly=False, log_data=False):
        super(DataTable, self).__init__(parent)

        self.headers = []

        self.data = []

        self.readonly = readonly

        self.table = QTableWidget()
        self.width = 0
        self.height = 0
        self.set_dimensions(width, height)

        if log_data:
            self.table.cellChanged.connect(self.cell_changed)
        self.table.verticalHeader().hide()

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.table)

        self.setLayout(self.vbox)

    # Utility functions
    def clear_table(self):
        self.table.clear()

    def set_dimensions(self, width=0, height=0):
        self.width = width
        self.height = height
        self.table.setColumnCount(width)
        self.table.setRowCount(height)

    def get_dimensions(self):
        return {"x": self.width, "y": self.height}

    def set_headers(self, headers):
        self.headers = headers
        self.table.setHorizontalHeaderLabels(headers)
        self.table.horizontalHeader().setStyleSheet('color:#1000A0')
        self.style_headers()

    def get_headers(self):
        return self.headers

    def style_headers(self, style="::section{background-color:#1000A0;color:white;font-weight:bold}"):
        self.table.horizontalHeader().setStyleSheet(style)
        self.table.horizontalHeader().setAutoFillBackground(True)

    def is_standard_var(self, var):
        var_type = type(var)

        if var_type is str:
            return True
        if var_type is int:
            return True
        if var_type is float:
            return True
        if var_type is complex:
            return True

    def build_combo(self, var):
        combo = QComboBox(self)
        combo.addItems(var)

        return combo

    def set_cell_tooltip(self, x=0, y=0, tooltip_text=""):
        self.table.item(y, x).setToolTip(tooltip_text)

    def set_cell_color(self, x=0, y=0, color="white"):
        """
        Method for setting the bg color of a cell

        Parameters
        ----------
        x : int
            Cell X co-ordinate
        y: int
            Cell Y co-ordinate
        color : string
            Color as to set cell background color

        Returns
        -------
        None
        """
        self.table.item(y, x).setBackgroundColor(QColor(color))

    def set_text_color(self, x=0, y=0, color="black"):
        """
        Method for setting the text color of a cell

        Parameters
        ----------
        x : int
            Cell X co-ordinate
        y: int
            Cell Y co-ordinate
        color : string
            Color to set cell text color

        Returns
        -------
        None
        """
        self.table.item(y, x).setTextColor(QColor(color))

    # Table data functions
    def add_row(self, row=[]):
        row_len = len(row)

        # General state of row parameter
        is_list = (type(row) is list)
        wider_than_table = (row_len > self.width)
        is_empty = (row_len == 0)

        if is_list:
            if not wider_than_table:
                y_index = self.height

                # Create blank row in table
                self.table.insertRow(y_index)

                # Add items to row in table
                for x_index in range(row_len):
                    contents = row[x_index]
                    if self.is_standard_var(contents):
                        contents = str(contents)
                        cell = QTableWidgetItem(contents)
                        if self.readonly:
                            cell.setFlags(Qt.ItemIsEditable)
                        self.table.setItem(y_index, x_index, cell)
                    elif type(contents) is bool:
                        check = QCheckBox(self)
                        check.setChecked(contents)
                        self.table.setCellWidget(y_index, x_index, check)
                    elif type(contents) is list:
                        combo = self.build_combo(contents)
                        self.table.setCellWidget(y_index, x_index, combo)
                self.height += 1

            else:
                raise Exception("Invalid Parameter: Row parameter is wider than table!")
        else:
            raise Exception("Invalid Parameter: Row parameter is not a list!")

    def insert_row(self, row=[], y_index=0):
        row_len = len(row)

        # State of row parameter
        is_list = (type(row) is list)
        wider_than_table = (row_len > self.width)

        # State of y_index
        index_within_bounds = (y_index < self.height)

        if is_list:
            if not wider_than_table:
                if index_within_bounds:
                    # Create blank row in table
                    self.table.insertRow(y_index)

                    # Add items to row in table
                    for x_index in range(row_len):
                        contents = row[x_index]
                        if self.is_standard_var(contents):
                            contents = str(contents)
                            cell = QTableWidgetItem(contents)
                            if self.readonly:
                                cell.setFlags(Qt.ItemIsEditable)
                            self.table.setItem(y_index, x_index, cell)
                        elif type(contents) is bool:
                            check = QCheckBox(self)
                            check.setChecked(contents)
                            self.table.setCellWidget(y_index, x_index, check)
                        elif type(contents) is list:
                            combo = self.build_combo(contents)
                            self.table.setCellWidget(y_index, x_index, combo)
                    self.height += 1
                else:
                    raise Exception("Invalid Parameter: y_index is out of bounds!")
            else:
                raise Exception("Invalid Parameter: Row parameter is wider than table!")
        else:
            raise Exception("Invalid Parameter: Row parameter is not a list!")

    def set_row(self, row=[], y_index=0):
        row_len = len(row)

        # State of row parameter
        is_list = (type(row) is list)
        wider_than_table = (row_len > self.width)

        # State of y_index
        index_within_bounds = (y_index < self.height)

        if is_list:
            if not wider_than_table:
                if index_within_bounds:
                    for x_index in range(row_len):
                        contents = row[x_index]
                        if self.is_standard_var(contents):
                            contents = str(contents)
                            cell = QTableWidgetItem(contents)
                            if self.readonly:
                                cell.setFlags(Qt.ItemIsEditable)
                            self.table.setItem(y_index, x_index, cell)
                        elif type(contents) is bool:
                            check = QCheckBox(self)
                            check.setChecked(contents)
                            self.table.setCellWidget(y_index, x_index, check)
                        elif type(contents) is list:
                            combo = self.build_combo(contents)
                            self.table.setCellWidget(y_index, x_index, combo)
                else:
                    raise Exception("Invalid Parameter: y_index is out of bounds!")
            else:
                raise Exception("Invalid Parameter: Row parameter is wider than table!")
        else:
            raise Exception("Invalid Parameter: Row parameter is not a list!")

    def get_row(self, y_index=0):
        # State of y_index
        index_within_bounds = (y_index < self.height)
        width = self.width

        row = []

        if index_within_bounds:
            for x_index in range(width):
                try:
                    cell = self.table.item(y_index, x_index)
                    cell_text = cell.text()
                    row.append(cell_text)
                except:
                    cell = self.table.cellWidget(y_index, x_index)
                    if isinstance(cell, QComboBox):
                        cell = cell.currentText()
                    elif isinstance(cell, QCheckBox):
                        cell = cell.isChecked()
                    row.append(cell)
            return row
        else:
            raise Exception("Invalid Parameter: y_index is out of bounds!")

    def remove_row(self, y_index=0):
        # State of y_index
        index_within_bounds = (y_index < self.height)

        if index_within_bounds:
            self.table.removeRow(y_index)
            self.height -= 1
        else:
            raise Exception("Invalid Parameter: y_index is out of bounds!")

    def load_table(self, data_arr=[]):
        try:
            width = len(data_arr[0])
            height = len(data_arr)

            self.set_dimensions(width)

            for item in data_arr:
                self.add_row(item)
        except IndexError as e:
            pass

    def get_all_rows(self):
        rows = []
        for y in range(self.height):
            rows.append(self.get_row(y))

        return rows

    def set_cell_text(self, x=0, y=0, text=""):
        """
        Method for setting the text content of a cell

        Parameters
        ----------
        x : int
            Cell X co-ordinate
        y: int
            Cell Y co-ordinate
        text : string
            Text to set cell content

        Returns
        -------
        None
        """
        cell = QTableWidgetItem(text)
        self.table.setItem(y, x, cell)

    def get_cell_text(self, x=0, y=0):
        """
        Method for Getting the text content of a cell

        Parameters
        ----------
        x : int
            Cell X co-ordinate
        y: int
            Cell Y co-ordinate

        Returns
        -------
        text_content : string
            Text content of specified cell
        """
        text_content = self.table.item(y, x).text()
        return text_content


if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    dt_table = DataTable(readonly=False)
    dt_table.set_dimensions(5)
    dt_table.set_headers(["","","","",""])
    dt_table.style_headers()

    mapping_options = ["option", "option", "option", "option", "option", "option"]
    mapping_row = [mapping_options, mapping_options, mapping_options, mapping_options, mapping_options]
    test_arr = [
                    mapping_row,
                    [False, "OLD", "OLD", "OLD", "OLD"],
                    [False, "OLD", "OLD", "OLD", "OLD"],
                    [False, "OLD", "OLD", "OLD", "OLD"],
                    [False, "OLD", "OLD", "OLD", "OLD"],
                ]

    dt_table.show()

    dt_table.load_table(test_arr)

    for i in range(dt_table.height):
        print(dt_table.get_row(i))

    sys.exit(qApp.exec_())
