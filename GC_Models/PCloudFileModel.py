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

    def load_data(self, file_dict={}):
        self.name = file_dict["name"]
        self.fileid = file_dict["fileid"]
        self.parent_folder_id = file_dict["parentfolderid"]
        self.created = file_dict["created"]
        self.modified = file_dict["modified"]
        self.thumb = file_dict["thumb"]
        self.size = file_dict["size"]
