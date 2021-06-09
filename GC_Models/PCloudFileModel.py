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
    def __init__(self):
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
                    f"\nFile Size: {self.size}\nPublink Code: {self.publink_code}\nFile Type: {self.file_type}\n"
        return f"-------------------------------------{file_data}-------------------------------------"
