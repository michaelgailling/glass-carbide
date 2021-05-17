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
                        main_path,asset_path,episode_path,animatics_path,sounds_path : LabeledDirectoryInput
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
