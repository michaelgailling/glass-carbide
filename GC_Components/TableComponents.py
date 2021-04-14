import sys
from PySide2.QtGui import QColor
from PySide2.QtWidgets import QFrame, QTableWidget, QVBoxLayout, QTableWidgetItem, QApplication


class DataTable(QFrame):
    def __init__(self, parent=None, width=0, height=0):
        super(DataTable, self).__init__(parent)
        self.table = QTableWidget()
        self.table.setColumnCount(width)
        self.table.setRowCount(height)
        self.table.cellChanged.connect(self.cell_changed)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.table)

        self.setLayout(self.vbox)

    def cell_changed(self, row, column):
        self.log_cell(column, row)

    def set_cell_color(self, x=0, y=0, color="white"):
        self.table.item(y, x).setBackgroundColor(QColor(color))

    def set_text_color(self, x=0, y=0, color="black"):
        self.table.item(y, x).setTextColor(QColor(color))

    def set_cell_contents(self, x=0, y=0, text=""):
        cell = QTableWidgetItem(text)
        self.table.setItem(y, x, cell)

    def get_cell_contents(self, x=0, y=0):
        return self.table.item(y, x).text()

    def log_cell(self, x, y):
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
    tab.show()
    sys.exit(qApp.exec_())
