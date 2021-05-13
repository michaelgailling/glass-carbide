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

from GC_Components.InputComponents import LabeledDirectoryInput


class ExistingDirectoryView(QFrame):
    def __init__(self, parent=None):
        super(ExistingDirectoryView, self).__init__(parent)

        self.directoryPath = LabeledDirectoryInput(self, label_text="Select Root Folder: ")

        self.main_layout = QVBoxLayout()

        self.main_layout.addWidget(self.directoryPath)
        self.setLayout(self.main_layout)
        self.setStyleSheet('LabeledDirectoryInput{border:none}')
        # self.setStyleSheet('border:none')
        # self.topLevelWidget().setStyleSheet('QFrame{border:none} '
        #                                    'LabeledDirectoryInput::QLineEdit{border:1px solid #1000A0}')
