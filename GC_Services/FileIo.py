import asyncio
import json
import os

class FileIo:
    """File IO

        Summary:
            A class for FileIo that includes:

            -Handles directory checking and creating

        Attributes:
            project_dir, asset_dir, episode_dir, animatic_dir, sound_dir

        Methods:
            validate_path, save_file_to_dir, make_dir, make_sub_dir

        Attributes
        ----------
            project_dir : str
                Root project directory path
            asset_dir : str
                Asset sub-directory path
            episode_dir : str
                Episode sub-directory path
            animatic_dir : str
                Animatics sub-directory path
            sound_dir : str
                Sounds sub-directory path

        Methods
        -------
            validate_path(self, path="")
                Validates the string parameter path exists
            save_file_to_dir(self, dir_path, filename, file_bytes)
                Saves file to directory
            make_dir(self, dir_path)
                Creates directories
            make_sub_dir(self, dir_path)
                Creates sub-directories

    """

    def __init__(self):
        """Constructor:
            Initialize file browsing service

            Parameters:
                self
            Returns:
                None
        """
        self.project_dir = ""
        self.asset_dir = ""
        self.episode_dir = ""
        self.animatic_dir = ""
        self.sound_dir = ""

    def validate_path(self, path=""):
        return os.path.exists(path)

    def save_file_to_dir(self, dir_path, filename, file_bytes):
        open(dir_path + "/" + filename, "wb").write(file_bytes)

    def make_dir(self, dir_path=""):
        try:
            os.makedirs(dir_path)
        except OSError:
            print("Fail - Directory Exists: %s " % dir_path)
        else:
            print("Success - Directory Created: %s " % dir_path)

    def make_sub_dir(self, dir_path):
        try:
            os.makedirs(self.project_dir + dir_path)
        except OSError:
            print("Fail - Directory Exists: %s " % dir_path)
        else:
            print("Success - Directory Created: %s " % dir_path)
