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
from GC_Services.FileIo import FileIo


class DirectoryMappingView(QFrame):
    """Directory Mapping View

                    Summary:
                        A class for {Type} that includes:

                        -{Description} to the {Location eg left}

                    Attributes:
                        label, {AttributeName}

                    Methods:
                        get_input_text, {MethodName}

                    Attributes
                    ----------
                        fio : FileIo
                            !!!File IO description!!!
                        mainPath,assetPath,episodePath,animaticsPath,soundsPath : LabeledDirectoryInput
                            {Property} for {Type}

                    Methods
                    -------
                        shared_dir_paths(self)
                            Return the text in the input box
                        make_dirs(self)
                            {Functionality}
                        dir_getter_filler(self)
                            {Functionality}
                        get_dir_path(self)
                            {Functionality}
                """
    def __init__(self, parent=None, file_io=FileIo()):
        super(DirectoryMappingView, self).__init__(parent)
        self.dir_path = ""
        self.fio = file_io
        self.mainPath = LabeledDirectoryInput(self, label_text="Project Directory: ", read_only=True)
        self.assetPath = LabeledDirectoryInput(self, label_text="Assets: ", read_only=True, btn_enable=False)
        self.episodePath = LabeledDirectoryInput(self, label_text="Episodes: ", read_only=True, btn_enable=False)
        self.animaticsPath = LabeledDirectoryInput(self, label_text="Animatics: ", read_only=True, btn_enable=False)
        self.soundsPath = LabeledDirectoryInput(self, label_text="Sounds: ", read_only=True, btn_enable=False)

        self.mainPath.open_directory_dialog = (lambda: self.shared_dir_paths())

        self.main_layout = QVBoxLayout()

        self.main_layout.addWidget(self.mainPath)
        self.main_layout.addWidget(self.assetPath)
        self.main_layout.addWidget(self.episodePath)
        self.main_layout.addWidget(self.animaticsPath)
        self.main_layout.addWidget(self.soundsPath)
        self.setLayout(self.main_layout)
        self.setStyleSheet('LabeledDirectoryInput{border:none}')

    def shared_dir_paths(self):
        self.dir_path = self.dir_getter_filler()
        self.fio.project_dir = self.dir_path
        if self.fio.project_dir:
            self.make_dirs()
            self.assetPath.set_input_text(f"{self.dir_path}/Assets")
            self.episodePath.set_input_text(f"{self.dir_path}/Episodes")
            self.animaticsPath.set_input_text(f"{self.dir_path}/Animatics")
            self.soundsPath.set_input_text(f"{self.dir_path}/Sounds")

    def make_dirs(self):
        if self.fio.project_dir:
            self.fio.make_dir("/Assets")
            self.fio.make_dir("/Episodes")
            self.fio.make_dir("/Animatics")
            self.fio.make_dir("/Sounds")

    def dir_getter_filler(self):
        directory_path = QFileDialog.getExistingDirectory(self, "Select a Directory")
        self.mainPath.set_input_text(directory_path)
        return directory_path

    def get_dir_path(self):
        return self.dir_path
