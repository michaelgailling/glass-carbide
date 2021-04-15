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


class DirectoryMappingView(QFrame):
    def __init__(self, parent=None):
        super(DirectoryMappingView, self).__init__(parent)

        self.mainPath = LabeledDirectoryInput(self, label_text="Project Directory: ")
        self.assetPath = LabeledDirectoryInput(self, label_text="Assets: ")
        self.episodePath = LabeledDirectoryInput(self, label_text="Episodes: ")
        self.animaticsPath = LabeledDirectoryInput(self, label_text="Animatics: ")
        self.soundsPath = LabeledDirectoryInput(self, label_text="Sounds: ")

        self.main_layout = QVBoxLayout()

        self.main_layout.addWidget(self.mainPath)
        self.main_layout.addWidget(self.assetPath)
        self.main_layout.addWidget(self.episodePath)
        self.main_layout.addWidget(self.animaticsPath)
        self.main_layout.addWidget(self.soundsPath)
        self.setLayout(self.main_layout)
