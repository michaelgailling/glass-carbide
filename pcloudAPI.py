import json

import requests


# https://api.pcloud.com/userinfo?getauth=1&logout=1&username={username}&password={password}
# https://api.pcloud.com/listfolder?auth={token}&folderid={folderid}

class PCloud:
    """PCloud API class

        Purpose:
            Handles connection from pCloud api service
        Attributes:

        Methods:

    """
    def __init__(self):
        """Constructor

            Parameters:
                self
            Returns:
                None
            Purpose:
                Initialize pCloud service
        """
        self.status_codes = {
            1000: "Log in required.",
            1004: "No fileid or path provided.",
            1005: "Unknown content-type requested.",
            1014: "Thumb can not be created from this file type.",
            1015: "Please provide valid thumb size. Width and height must be divisible either by 4 or 5 and must be "
                  "between 16 and 2048 (1024 for height).",
            1016: "No full topath or toname/tofolderid provided.",
            1017: "Invalid 'folderid' provided.",
            1018: "Invalid 'fileid' provided.",
            1022: "Please provide 'code'.",
            1025: "Please provide 'sharerequestid' or 'code' to accept a share.",
            1026: "Please provide 'sharerequestid'.",
            1027: "Please provide 'shareid'.",
            1031: "Please provide 'oldpassword'.",
            1032: "Please provide 'newpassword'.",
            1033: "Please provide 'mail'.",
            1034: "Please provide 'password'.",
            1037: "Please provide at least one of 'topath', 'tofolderid' or 'toname'.",
            1038: "Please provide 'fileids'.",
            1040: "Please provide 'url'.",
            1052: "Please provide 'progresshash'.",
            1074: "Expired 'code' provided.",
            1076: "Please provide 'tokenid'.",
            1900: "Upload not found.",
            2000: "Log in failed.",
            2001: "Invalid file/folder name.",
            2002: "A component of parent directory does not exist.",
            2003: "Access denied.You do not have permissions to preform this operation.",
            2004: "File or folder already exists.",
            2005: "Directory does not exist.",
            2008: "User is over quota.",
            2009: "File not found.",
            2010: "Invalid path.",
            2011: "Requested speed limit too low, see minspeed for minimum.",
            2012: "Invalid 'code' provided.",
            2013: "Email is already verified.",
            2014: "Please verify your email address to preform this action.",
            2015: "Can not share root folder.",
            2016: "You can only share your own folders.",
            2017: "User does not accept shares.",
            2018: "Invalid 'mail' provided.",
            2019: "Share request already exists.",
            2020: "You can't share a folder with yourself.",
            2021: "Non existing share request. It might be already accepted or cancelled by the sending user.",
            2022: "Wrong user to accept the share.",
            2023: "You are trying to place shared folder into another shared folder.",
            2024: "User already has access to this folder or subfolder of this folder.",
            2025: "Invalid shareid.",
            2030: "New password is the same as the old one.",
            2031: "Wrong 'oldpassword' provided.",
            2032: "Password too short. Minimum length is 6 characters.",
            2033: "Password can not start or end with space.",
            2034: "Password does not contain enough different characters. The minimum is 4.",
            2035: "Password can not contain only consecutive characters.",
            2036: "Verification 'code' expired. Please request password reset again.",
            2037: "You need to accept Terms of Service and all other agreements to register.",
            2038: "User with this email is already registered.",
            2039: "You have to own the folder for upload.",
            2040: "Given 'uploadlinkid' not found.",
            2041: "Connection broken.",
            2044: "Video links can only be generated for videos.",
            2059: "Unsupported archive format.",
            2061: "Unsupported character set in 'fromecoding' or 'toencoding'.",
            2271: "User is already with this mail.",
            2271: "Wrong 'password' provided.",
            3006: "Extracting of the archive failed.",
            4000: "Too many login tries from this IP address.",
            5000: "Internal error.Try again later.",
            5001: "Internal upload error.",
            5002: "Internal error, no servers available. Try again later.",
            7002: "This link is deleted by the owner.",
            7004: "This link has expired.",
            7007: "This link has reached its space limit.",
            7008: "This link has reached its file limit."
        }

        self.regionUrlDict = {
            "NA": "https://api.pcloud.com/",
            "EU": "https://eapi.pcloud.com/"
        }

        self.methodParamDict = {
            "userinfo":
                {
                    "getauth": "1",
                    "logout": "1",
                    "username": None,
                    "password": None
                },
            "listfolder":
                {
                    "auth": None,
                    "folderid": "0"
                }
        }

        self.username = None
        self.password = None
        self.region = None
        self.token = ""
        self.folderId = "0"

    async def auth(self, username=None, password=None, region="NA"):

        method_params = self.methodParamDict["userinfo"]

        self.region = region

        override = username and password

        if override:
            self.username = username
            self.password = password

        valid_login = self.username and self.password

        if valid_login:
            method_params["username"] = self.username
            method_params["password"] = self.password

            url = self.regionUrlDict[self.region] + "userinfo"

            res = requests.get(url, params=method_params)
        else:
            print("Error encountered: Invalid login details before request!")
            return

        status_code = res.status_code

        if status_code == 200:
            res_obj = json.loads(res.text)
            self.token = res_obj["auth"]
        elif status_code == 1000:
            print("Error 1000 encountered: Log in required!")
        elif status_code == 2000:
            print("Error 2000 encountered: Log in failed!")
        elif status_code == 3000:
            print("Error 3000 encountered: Too many login tries from this IP address!")

    async def list_folder(self, folder_id="0"):
        method_params = self.methodParamDict["listfolder"]
        method_params["auth"] = self.token
        method_params["folderid"] = folder_id
        valid_token = self.token is not None

        if valid_token:
            url = self.regionUrlDict[self.region] + "listfolder"

            res = requests.get(url, params=method_params)

        status_code = res.status_code()

        if status_code == 200:
            res_obj = json.loads(res.text)
            return res_obj
        elif status_code == 1000:
            print("Error 1000 encountered: Log in required!")
        elif status_code == 2000:
            print("Error 2000 encountered: Log in failed!")
        elif status_code == 3000:
            print("Error 3000 encountered: Too many login tries from this IP address!")



apic = PCloud()

apic.auth("hitujy@zetmail.com", "test12345678")
print(apic.token)




