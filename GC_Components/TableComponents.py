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
import sys
from PySide2.QtGui import QColor, Qt
from PySide2.QtWidgets import QFrame, QTableWidget, QVBoxLayout, QTableWidgetItem, QApplication, QWidget, QComboBox, \
    QCheckBox, QHeaderView


class DataTable(QFrame):
    """Labeled Input

        Summary:
            A class for a data table that includes:

            -Method for altering cell bg color

            -Method for altering cell text color

            -Method for setting and getting cell values

        Attributes:
            table

        Methods:
            cell_changed, set_cell_color, set_text_color, set_cell_contents, get_cell_contents, log_cell

        Attributes
        ----------
            table : QTable
                Table for holding data

        Methods
        -------
            cell_changed(self, y, x)
                Slot for cell changed signal
            set_cell_color(self, x=0, y=0, color="white")
                Sets the background color of the specified cell
            set_text_color(self, x=0, y=0, color="black")
                Sets the text color of the specified cell
            set_cell_contents(self, x=0, y=0, text="")
                Sets the contents of the specified cell
            get_cell_contents(self, x=0, y=0)
                Gets the contents of the specified cell
            log_cell(self, x, y)
                Prints info about the specified cell
    """
    def __init__(self, parent=None, width=0, height=0, log_data=False):
        """
        Constructs all the necessary attributes for the Data Table object.

        Parameters
        ----------
            parent : QWidget
            width : int
                The number of columns
            height : int
                The number of rows
        """
        super(DataTable, self).__init__(parent)

        self.mappings = []
        self.selections = []

        self.table = QTableWidget()
        self.width = width
        self.height = height
        self.set_dimensions(width, height)

        if log_data:
            self.table.cellChanged.connect(self.cell_changed)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.table)

        self.setLayout(self.vbox)

    def clear_table(self):
        self.table.clear()

    def set_dimensions(self, width=0, height=0):
        self.width = width
        self.height = height
        self.table.setColumnCount(width)
        self.table.setRowCount(height)

    def set_headers(self, headers):
        self.table.setHorizontalHeaderLabels(headers)
        self.table.horizontalHeader().setStyleSheet('color:blue')

    def insert_control_row(self, widget_type=None, start_index=0, options=[]):
        self.table.insertRow(0)

        self.height += 1

        if widget_type:
            width = self.width
            self.mappings = []
            for x in range(start_index, width):
                self.mappings.append(self.create_control_widget(widget_type, options))
                self.set_cell_widget(self.mappings[-1], x, 0)

    def insert_control_column(self, widget_type=None, start_index=0, options=[]):
        self.table.insertColumn(0)

        self.width += 1

        if widget_type:
            height = self.height
            self.selections = []
            for y in range(start_index, height):
                self.selections.append(self.create_control_widget(widget_type, options))
                self.set_cell_widget(self.selections[-1], 0, y)

    def create_control_widget(self, widget_type=None, options=[]):
        if widget_type == "combobox":
            widget = QComboBox()

            widget.setEditable(True)

            if options:
                widget.addItems(options)

        elif widget_type == "checkbox":
            widget = QCheckBox(self)

        return widget

    def load_data(self, data=[]):
        height = len(data)
        width = len(data[0])

        self.set_dimensions(width, height)

        for y in range(height):
            for x in range(width):
                cell = QTableWidgetItem(data[y][x])
                self.table.setItem(y, x, cell)

        header = self.table.horizontalHeader()
        self.table.verticalHeader().hide()
        for i in range(width):
            header.setSectionResizeMode(i, QHeaderView.ResizeToContents)

    def cell_changed(self, y=0, x=0):
        """
        Slot for handling cell change events

        Parameters
        ----------
        x : int
            Cell X co-ordinate
        y: int
            Cell Y co-ordinate

        Returns
        -------
        None
        """
        asyncio.run(self.log_cell(x, y))

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

    def set_cell_widget(self,  widget=None, x=0, y=0,):
        self.table.setCellWidget(y, x, widget)

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

    async def log_cell(self, x=0, y=0):
        """
        Method for logging the current state of a cell to console

        Parameters
        ----------
        x : int
            Cell X co-ordinate
        y: int
            Cell Y co-ordinate

        Returns
        -------
        None
        """
        cell_text = self.get_cell_text(x, y)
        bg_color_red = str(self.table.item(y, x).backgroundColor().red())
        bg_color_green = str(self.table.item(y, x).backgroundColor().green())
        bg_color_blue = str(self.table.item(y, x).backgroundColor().blue())
        bg_color_alpha = str(self.table.item(y, x).backgroundColor().alpha())
        text_color_red = str(self.table.item(y, x).textColor().red())
        text_color_green = str(self.table.item(y, x).textColor().green())
        text_color_blue = str(self.table.item(y, x).textColor().blue())
        text_color_alpha = str(self.table.item(y, x).textColor().alpha())

        print()
        print()

        print("Cell Changed")
        print("-------------------------------------")
        print("x:" + str(x) + " y:" + str(y))
        print()

        print("Cell Data")
        print("-------------------------------------")
        print(cell_text)
        print()

        print("Background Color")
        print("-------------------------------------")
        print("RED: " + bg_color_red + " GREEN: " + bg_color_green + " BLUE: " + bg_color_blue +
              " ALPHA: " + bg_color_alpha)
        print()

        print("Text Color")
        print("-------------------------------------")
        print("RED: " + text_color_red + " GREEN: " + text_color_green + " BLUE: " + text_color_blue +
              " ALPHA: " + text_color_alpha)

        print()
        print()


class MappableDataTable(DataTable):
    def __init__(self, parent):
        super(MappableDataTable, self).__init__(parent)

        self.mappings = []


if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    tab = DataTable(width=2, height=1)
    tab.set_cell_text(0, 0, "Hello")
    tab.set_cell_color(0, 0, "red")
    tab.set_cell_text(1, 0, "World")
    tab.set_cell_color(1, 0, "Green")
    tab.show()
    sys.exit(qApp.exec_())
