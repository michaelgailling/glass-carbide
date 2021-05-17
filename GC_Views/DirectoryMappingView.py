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


from PySide2.QtWidgets import QFrame, QVBoxLayout, QFileDialog, QPushButton
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
        self.main_path = LabeledDirectoryInput(self, label_text="Project Directory: ", read_only=True)
        self.asset_path = LabeledDirectoryInput(self, label_text="Assets: ", read_only=True)
        self.episode_path = LabeledDirectoryInput(self, label_text="Episodes: ", read_only=True)
        self.animatics_path = LabeledDirectoryInput(self, label_text="Animatics: ", read_only=True)
        self.sounds_path = LabeledDirectoryInput(self, label_text="Sounds: ", read_only=True)

        self.btn_create_directory = QPushButton(parent=self, text="Create New Directories")

        self.main_path.open_directory_dialog = (lambda: self.shared_dir_paths())
        self.btn_create_directory.clicked.connect(self.make_dirs)

        self.vbl_main_layout = QVBoxLayout(self)

        self.vbl_main_layout.addWidget(self.ldi_main_path)
        self.vbl_main_layout.addWidget(self.ldi_asset_path)
        self.vbl_main_layout.addWidget(self.ldi_episode_path)
        self.vbl_main_layout.addWidget(self.ldi_animatics_path)
        self.vbl_main_layout.addWidget(self.ldi_sounds_path)
        self.vbl_main_layout.addWidget(self.btn_create_new_directory)
        self.setLayout(self.vbl_main_layout)
        self.setStyleSheet('LabeledDirectoryInput{border:none}')

    def shared_dir_paths(self):
        self.show_directory_dialog()
        self.fio.project_dir = self.main_path.get_input_text()

        if self.fio.project_dir:
            self.asset_path.set_input_text(f"{self.dir_path}/Assets")
            self.episode_path.set_input_text(f"{self.dir_path}/Episodes")
            self.animatics_path.set_input_text(f"{self.dir_path}/Animatics")
            self.sounds_path.set_input_text(f"{self.dir_path}/Sounds")

    def make_dirs(self):
        if self.fio.project_dir:
            self.fio.asset_dir = self.ldi_asset_path.get_input_text()
            self.fio.episode_dir = self.ldi_episode_path.get_input_text()
            self.fio.animatic_dir = self.ldi_animatics_path.get_input_text()
            self.fio.sound_dir = self.ldi_sounds_path.get_input_text()
            self.fio.make_dir("/Assets")
            self.fio.make_dir("/Episodes")
            self.fio.make_dir("/Animatics")
            self.fio.make_dir("/Sounds")

    def show_directory_dialog(self):
        directory_path = QFileDialog.getExistingDirectory(self, "Select a Directory")
        self.ldi_main_path.set_input_text(directory_path)
