import asyncio
import sys
from PySide2.QtGui import QColor
from PySide2.QtWidgets import QFrame, QTableWidget, QVBoxLayout, QTableWidgetItem, QApplication


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
        self.table = QTableWidget()
        self.set_dimensions(width, height)

        if log_data:
            self.table.cellChanged.connect(self.cell_changed)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.table)

        self.setLayout(self.vbox)

    def set_dimensions(self, width, height):
        self.table.setColumnCount(width)
        self.table.setRowCount(height)

    def cell_changed(self, y, x):
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

    def set_cell_contents(self, x=0, y=0, text=""):
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

    def get_cell_contents(self, x=0, y=0):
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

    async def log_cell(self, x, y):
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
        cell_text = self.get_cell_contents(x, y)
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


if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    tab = DataTable(width=2, height=1)
    tab.set_cell_contents(0, 0, "Hello")
    tab.set_cell_color(0, 0, "red")
    tab.set_cell_contents(1, 0, "World")
    tab.set_cell_color(1, 0, "Green")
    tab.show()
    sys.exit(qApp.exec_())
