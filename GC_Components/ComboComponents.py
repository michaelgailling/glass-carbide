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
    """Embeddable ComboBox

            Summary:
                A class for {Type} that includes:

                -{Description} to the {Location eg left}

            Attributes:
                combo, hbox

            Methods:
                current_text, set_editable, add_items

            Attributes
            ----------
                combo : QComboBox
                    Text Label for Input Box
                hbox : QHBoxLayout
                    {Property} for {Type}

            Methods
            -------
                current_text(self):
                    Returns combo box text
                set_editable(self, editable=False):
                    Sets combo box as editable
                add_items(self, items)
                    Adds list item to combo box
        """
    def __init__(self, parent=None):
        """
                Constructs all the necessary attributes for the EmbeddableCombBox  object.

                Parameters
                ----------
                    self
                    parent : QWidget
                """
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
