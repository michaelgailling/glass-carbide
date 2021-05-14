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
                        A class for mapping of directories that includes:

                        -{Description} stacked vertically in the center

                    Attributes:
                        main_layout, fio, mainPath, assetPath, episodePath, animaticsPath, soundsPath

                    Methods:
                        get_input_text, make_dirs, dir_getter_filler, get_dir_path

                    Attributes
                    ----------
                        main_layout : QVBoxLayout
                        dir_path : str
                            Stores direct path for selected root folder
                        fio : FileIo
                            !!! File input & output
                        mainPath : LabeledDirectoryInput
                            Labeled Directory Input for root directory path
                        assetPath: LabeledDirectoryInput
                            Labeled Directory Input for asset directory path
                        episodePath : LabeledDirectoryInput
                            Labeled Directory Input for episode directory path
                        animaticsPath : LabeledDirectoryInput
                            Labeled Directory Input for animatics directory path
                        soundsPath : LabeledDirectoryInput
                            Labeled Directory Input for sounds directory path

                    Methods
                    -------
                        shared_dir_paths(self)
                            !!! Auto-generates sub-directory paths
                        make_dirs(self)
                            Create directories/folders in root directory
                        dir_getter_filler(self)
                            !!! Passes root directory path to TableView
                        get_dir_path(self)
                            Returns directory path
                """
    def __init__(self, parent=None, file_io=FileIo()):
        """Constructor:
                    Initialize Directory Mapping View

                    Parameters:
                        self
                        parent : QFrame
                        file_io : FileIo
                            File input & output
                    Returns:
                        None
                """
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
