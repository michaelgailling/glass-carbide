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
from PySide2.QtWidgets import QFrame, QVBoxLayout, QFileDialog, QPushButton, QMessageBox
from GC_Components.InputComponents import LabeledDirectoryInput
from GC_Services.FileIo import FileIo


class GCCreateDirectoryView(QFrame):
    """Directory Mapping View

                    Summary:
                        A class for creating directories that includes:

                        -LabeledDirectoryInputs in a vertical layout
                        -Button for creating new directories

                    Attributes:
                        label, ldi_main_path, ldi_asset_path, ldi_episode_path, ldi_animatics_path, ldi_sounds_path,
                        vbl_main_layout, btn_create_new_directory

                    Methods:
                        plan_dir_structure, create_dir_structure, show_directory_dialog, fill_directory_listings,
                        make_dirs, update_fio

                    Attributes
                    ----------
                        fio : FileIo
                            !!!File IO description!!!
                        vbl_main_layout : QVBoxLayout
                            Main vertical layout
                        ldi_main_path : LabeledDirectoryInput
                            LabeledDirectoryInput for project root directory
                        ldi_asset_path : LabeledDirectoryInput
                            LabeledDirectoryInput for assets directory
                        ldi_episode_path : LabeledDirectoryInput
                            LabeledDirectoryInput for episodes directory
                        ldi_animatics_path : LabeledDirectoryInput
                            LabeledDirectoryInput for animatics directory
                        ldi_sounds_path : LabeledDirectoryInput
                            LabeledDirectoryInput for sounds directory
                        btn_create_new_directory: QPushButton
                            Button for creating new directories

                    Methods
                    -------
                        plan_dir_structure(self):
                            {Functionality}
                        create_dir_structure(self):
                            Validates root directory path & calls make_dirs method
                        show_directory_dialog(self):
                            Sets input path to File Dialog selection
                        fill_directory_listings(self):
                            Sets subdirectory paths based on main_path
                        make_dirs(self):
                            Creates new directories
                        update_fio(self):
                            Updates fio
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
        super(GCCreateDirectoryView, self).__init__(parent)
        self.fio = file_io
        self.ldi_main_path = LabeledDirectoryInput(None, label_text="Project Directory: ", read_only=True)
        self.ldi_asset_path = LabeledDirectoryInput(None, label_text="Assets: ", read_only=True)
        self.ldi_episode_path = LabeledDirectoryInput(None, label_text="Episodes: ", read_only=True)
        self.ldi_animatics_path = LabeledDirectoryInput(None, label_text="Animatics: ", read_only=True)
        self.ldi_sounds_path = LabeledDirectoryInput(None, label_text="Sounds: ", read_only=True)

        self.btn_create_new_directory = QPushButton(text="Create New Directories")

        self.ldi_main_path.open_directory_dialog = self.plan_dir_structure
        self.btn_create_new_directory.clicked.connect(self.create_dir_structure)

        self.vbl_main_layout = QVBoxLayout()

        self.vbl_main_layout.addWidget(self.ldi_main_path)
        self.vbl_main_layout.addWidget(self.ldi_asset_path)
        self.vbl_main_layout.addWidget(self.ldi_episode_path)
        self.vbl_main_layout.addWidget(self.ldi_animatics_path)
        self.vbl_main_layout.addWidget(self.ldi_sounds_path)
        self.vbl_main_layout.addWidget(self.btn_create_new_directory, alignment=Qt.AlignHCenter)
        self.setLayout(self.vbl_main_layout)
        self.setStyleSheet('border:none;')
        self.topLevelWidget().setStyleSheet('QFrame{border:none} '
                                            'LabeledDirectoryInput::QLineEdit{border:1px solid #1000A0}')

    def plan_dir_structure(self):
        self.show_directory_dialog()
        valid_path = self.fio.validate_path(self.ldi_main_path.get_input_text())
        if valid_path:
            self.fill_directory_listings()
        else:
            msg_warning = QMessageBox()
            msg_warning.setIcon(QMessageBox.Warning)
            msg_warning.setText("Invalid directory path entered!")
            msg_warning.exec_()

    def create_dir_structure(self):
        valid_path = self.fio.validate_path(self.ldi_main_path.get_input_text())
        if valid_path:
            self.make_dirs()
            self.update_fio()
        else:
            msg_warning = QMessageBox()
            msg_warning.setIcon(QMessageBox.Warning)
            msg_warning.setText("Invalid directory path entered! Cannot Create!")
            msg_warning.exec_()

    def show_directory_dialog(self):
        directory_path = QFileDialog.getExistingDirectory(self, "Select a Directory")
        if len(directory_path) > 6:
            self.ldi_main_path.set_input_text(directory_path)

    def fill_directory_listings(self):
        dir_path = self.ldi_main_path.get_input_text()
        self.ldi_asset_path.set_input_text(f"{dir_path}/Assets")
        self.ldi_episode_path.set_input_text(f"{dir_path}/Episodes")
        self.ldi_animatics_path.set_input_text(f"{dir_path}/Animatics")
        self.ldi_sounds_path.set_input_text(f"{dir_path}/Sounds")

    def make_dirs(self):
        self.fio.make_dir(self.ldi_main_path.get_input_text())
        self.fio.make_dir(self.ldi_asset_path.get_input_text())
        self.fio.make_dir(self.ldi_episode_path.get_input_text())
        self.fio.make_dir(self.ldi_animatics_path.get_input_text())
        self.fio.make_dir(self.ldi_sounds_path.get_input_text())

    def update_fio(self):
        self.fio.project_dir = self.ldi_main_path.get_input_text()
        self.fio.asset_dir = self.ldi_asset_path.get_input_text()
        self.fio.episode_dir = self.ldi_episode_path.get_input_text()
        self.fio.animatic_dir = self.ldi_animatics_path.get_input_text()
        self.fio.sound_dir = self.ldi_sounds_path.get_input_text()
