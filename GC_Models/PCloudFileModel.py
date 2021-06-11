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

class PCloudFileModel:
    """PCloudFileModel

            Summary:
                A class that models PCloud file results

            Attributes:
                name, fileid, parent_folder_id, created, modified, thumb, size, publink_code, file_type

            Methods:
                load_data, __str__

            Attributes
            ----------
                name : str
                fileid : str
                parent_folder_id : str
                created : str
                modified = ""
                thumb : bool
                size : int
                publink_code : str
                file_type : str
            Methods
            -------
                load_data(self, file_dict={})
                    Parses data from dictionary
                __str__(self)
                    Returns string representation

    """
    def __init__(self):
        """
            Constructs all the necessary attributes for the PCloudFileModel object.

            Parameters
            ----------
                self
        """
        self.name = ""
        self.fileid = ""
        self.parent_folder_id = ""
        self.created = ""
        self.modified = ""
        self.thumb = False
        self.size = 0
        self.publink_code = ""
        self.file_type = ""
        self.ignore = False

    def load_data(self, file_dict={}):
        self.name = file_dict["name"]
        self.fileid = file_dict["fileid"]
        self.parent_folder_id = file_dict["parentfolderid"]
        self.created = file_dict["created"]
        self.modified = file_dict["modified"]
        self.thumb = file_dict["thumb"]
        self.size = file_dict["size"]

    def __str__(self):
        file_data = f"\nFilename: {self.name} \nFile ID: {self.fileid} \nParent Folder ID: {self.parent_folder_id} " \
                    f"\nCreated: {self.created} \nModified: {self.modified} \nThumbnail Available: {self.thumb} " \
                    f"\nFile Size: {self.size} Bytes\nPublink Code: {self.publink_code}\nFile Type: {self.file_type}" \
                    f"\nIgnore File: {self.ignore}\n"
        return f"-------------------------------------{file_data}-------------------------------------"
