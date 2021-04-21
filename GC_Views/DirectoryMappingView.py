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


from PySide2.QtWidgets import QFrame, QVBoxLayout, QFileDialog

from GC_Components.InputComponents import LabeledDirectoryInput


class DirectoryMappingView(QFrame):
    def __init__(self, parent=None):
        super(DirectoryMappingView, self).__init__(parent)

        self.dir_path = ""

        self.mainPath = LabeledDirectoryInput(self, label_text="Project Directory: ")
        self.assetPath = LabeledDirectoryInput(self, label_text="Assets: ")
        self.episodePath = LabeledDirectoryInput(self, label_text="Episodes: ")
        self.animaticsPath = LabeledDirectoryInput(self, label_text="Animatics: ")
        self.soundsPath = LabeledDirectoryInput(self, label_text="Sounds: ")

        self.mainPath.open_directory_dialog = (lambda: self.shared_dir_paths())

        self.main_layout = QVBoxLayout()

        self.main_layout.addWidget(self.mainPath)
        self.main_layout.addWidget(self.assetPath)
        self.main_layout.addWidget(self.episodePath)
        self.main_layout.addWidget(self.animaticsPath)
        self.main_layout.addWidget(self.soundsPath)
        self.setLayout(self.main_layout)

    def shared_dir_paths(self):
        self.dir_path = self.dir_getter_filler()
        self.assetPath.set_input_text(f"{self.dir_path}/Assets")
        self.episodePath.set_input_text(f"{self.dir_path}/Episodes")
        self.animaticsPath.set_input_text(f"{self.dir_path}/Animatics")
        self.soundsPath.set_input_text(f"{self.dir_path}/Sounds")

    def dir_getter_filler(self):
        directory_path = QFileDialog.getExistingDirectory(self, "Select a Directory")
        self.mainPath.set_input_text(directory_path)
        return directory_path

