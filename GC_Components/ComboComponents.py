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
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QWidget, QComboBox, QHBoxLayout


class EmbeddableComboBox(QWidget):
    def __init__(self, parent=None):
        super(EmbeddableComboBox, self).__init__(parent)

        self.combo = QComboBox()

        self.hbox = QHBoxLayout(self)

        self.hbox.addWidget(self.combo)

        self.hbox.setAlignment(Qt.AlignCenter)
        self.hbox.setContentsMargins(0, 0, 0, 0)

    def current_text(self):
        return self.combo.currentText()

    def set_editable(self, editable=False):
        self.combo.setEditable(editable)

    def add_items(self, items):
        self.combo.addItems(items)
