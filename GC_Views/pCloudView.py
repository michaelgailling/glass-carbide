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


from PySide2.QtWidgets import QFrame, QVBoxLayout

from GC_Components.InputComponents import LabeledInputWithButton


class PCloudView(QFrame):
    def __init__(self, parent=None):
        super(PCloudView, self).__init__(parent)

        self.pCloudPath = LabeledInputWithButton(self, label_text="Public Shared Link: ", button_text="Open")

        self.main_layout = QVBoxLayout()

        self.main_layout.addWidget(self.pCloudPath)
        self.setLayout(self.main_layout)


