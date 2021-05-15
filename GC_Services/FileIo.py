import asyncio
import json
import os


class FileIo:
    """File IO

                Summary:
                    A class for {Type} that includes:

                    -{Description} to the {Location eg left}

                Attributes:
                    project_dir, asset_dir, episode_dir, animatic_dir, sound_dir

                Methods:
                    save_file_to_dir, make_dir

                Attributes
                ----------
                    project_dir : str
                        Root directory path
                    asset_dir : str
                        Asset directory path
                    episode_dir : str
                        Episode directory path
                    animatic_dir : str
                        Animatics directory path
                    sound_dir : str
                        Sounds directory path

                Methods
                -------
                    save_file_to_dir(self, dir_path, filename, file_bytes)
                        Saves file to directory
                    make_dir(self, dir_path)
                        Creates directories
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

    def save_file_to_dir(self, dir_path, filename, file_bytes):
        open(dir_path + "/" + filename, "wb").write(file_bytes)

    def make_dir(self, dir_path):
        try:
            os.makedirs(self.project_dir + dir_path)
        except OSError:
            print("Fail - Directory Exists: %s " % dir_path)
        else:
            print("Success - Directory Created: %s " % dir_path)

# fio = FileIo()

# fio.make_dir("C:/Work/Outrageous/FileDump/Episode19/Assets/chars")
#
# fio.project_dir = "C:/Work/Outrageous/FileDump"

# apic = PCloud()
#
# apic.set_region("NA")
# pub_link_dir = asyncio.run(apic.show_pub_link_directory("kZXpOjXZnGCxvIiKSzJbuYQUiakTARUrXj7V"))
#
# pub_link_download = asyncio.run(apic.get_pub_link_download(code="kZXpOjXZnGCxvIiKSzJbuYQUiakTARUrXj7V", file_id="27739405968"))
#
# host = "http://" + pub_link_download["hosts"][0]
# path = pub_link_download["path"]
#
# url = host + path
#
# file_res = asyncio.run(apic.download_file(url))
#
# fio.save_file_to_dir("TEST.jpg", file_res)


