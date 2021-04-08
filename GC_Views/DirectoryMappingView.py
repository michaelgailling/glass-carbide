from PySide2.QtWidgets import QFrame, QLabel, QHBoxLayout, QVBoxLayout, QLineEdit

from GC_Components.InputComponents import LabeledInput, LabeledPathInput


class DirectoryMappingView(QFrame):
    def __init__(self, parent=None):
        super(DirectoryMappingView, self).__init__(parent)

        self.mainPath = LabeledPathInput(self, "Project Directory")
        self.assetPath = LabeledPathInput(self, "Assets")
        self.episodePath = LabeledPathInput(self, "Episodes")
        self.animaticsPath = LabeledPathInput(self, "Animatics")
        self.soundsPath = LabeledPathInput(self, "Sounds")

        self.main_layout = QVBoxLayout()

        self.main_layout.addWidget()
        self.setLayout(self.main_layout)