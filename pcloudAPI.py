import asyncio
import json
from hashlib import sha1
from typing import Dict

import requests
# https://api.pcloud.com/userinfo?getauth=1&logout=1&username={username}&password={password}
# https://api.pcloud.com/listfolder?auth={token}&folderid={folderid}


class PCloud:
    """PCloud API class:
        Handles connection from pCloud api service

        Attributes:

        Methods:

    """

    def __init__(self):
        """Constructor:
            Initialize pCloud service

            Parameters:
                self
            Returns:
                None
        """
        self.result_codes = {
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

        self.methodParamDict = {
            "auth":
                {
                    "getauth": "1",
                    "logout": "1"
                },
            "auth_digest":
                {
                    "digest": None,
                    "passworddigest": None
                },
            "validate_token":
                {

                },
            "listfolder":
                {
                    "auth": None,
                    "folderid": 0
                },
            "createfolder":
                {
                    "auth": None,
                    "name": None,
                    "folderid": 0
                },
            "renamefolder":
                {
                    "auth": None,
                    "folderid": None,
                    "toname": None
                },
            "deletefolder":
                {
                    "auth": None,
                    "folderid": None
                }
        }

        self.regionUrlDict = {
            "NA": "https://api.pcloud.com/",
            "EU": "https://eapi.pcloud.com/"
        }

        self.user_details = {
            "username": None,
            "password": None
        }

        self.regionUrl = None
        self.token = ""
        self.folderId = "0"

################ Helpers #######################
    def set_region(self, region="NA"):

        valid_region = bool(region in self.regionUrlDict.keys())

        if valid_region:
            self.regionUrl = self.regionUrlDict[region]
            return True
        else:
            return False

    def set_username(self, username):

        if username:
            self.user_details["username"] = username
            return True
        else:
            return False

    def set_password(self, password):

        if password:
            self.user_details["password"] = password
            return True
        else:
            return False

    def user_details_valid(self):
        valid_username = bool(self.user_details["username"])
        valid_password = bool(self.user_details["password"])

        if valid_username and valid_password:
            return True
        else:
            return False

    def handle_status_code(self, response):
        status_code = response.status_code

        if status_code == 200:
            res_obj = json.loads(response.text)
            return res_obj
        else:
            print("Unexpected error encountered: " + str(status_code) + " " + response.text)
            return False

    def handle_result_code(self, result_code=None):
        if result_code == 0:
            return True
        elif result_code in self.result_codes.keys():
            print("Result Code Error: " + str(result_code) + " - " + self.result_codes[result_code])
            return False

    def valid_token(self):
        return self.token is not None

################ Insecure Login #######################
    async def auth(self):
        if self.user_details_valid() and self.regionUrl:
            method_params = self.methodParamDict["auth"]
            method_params.update(self.user_details)

            url = self.regionUrl + "userinfo"

            res = requests.get(url, params=method_params)
        else:
            print("Error encountered: Invalid login details before request!")
            return False

        if res_obj := self.handle_status_code(res):
            res_obj = json.loads(res.text)
            result_code = res_obj["result"]

            if self.handle_result_code(result_code):
                self.token = res_obj["auth"]

        self.set_password(None)

################ Secure Login #######################
    async def get_digest(self):
        url = self.regionUrl + "getdigest"
        method_params = None
        res = requests.get(url, params=method_params)
        digest = json.loads(res.text)

        return digest["digest"]

    def create_password_digest(self, digest):
        username = str(self.user_details["username"]).lower().encode('utf-8')
        username_digest = sha1(username).hexdigest().encode('utf-8')
        password = str(self.user_details["password"]).encode('utf-8')
        digest = str(digest).encode('utf-8')
        password_digest = sha1(password + username_digest + digest).hexdigest()

        return password_digest

    async def auth_digest(self):

        if self.user_details_valid() and self.regionUrl:
            digest = await self.get_digest()
            password_digest = self.create_password_digest(digest)

            digest_login = {
                "username": self.user_details["username"],
                "digest": digest,
                "passworddigest": password_digest,
                "getauth": "1",
                "logout": "1"
            }

            method_params = digest_login
            url = self.regionUrl + "userinfo"
            res = requests.get(url, params=method_params)

        else:
            print("Error encountered: Invalid login details before request!")
            return False

        if res_obj := self.handle_status_code(res):
            res_obj = json.loads(res.text)
            result_code = res_obj["result"]

            if self.handle_result_code(result_code):
                self.token = res_obj["auth"]

        self.set_password(None)

    async def auth2(self):
        pass

################ Folder Methods #######################
    async def list_folder(self, folder_id=None):

        if self.valid_token() and folder_id:
            method_params = self.methodParamDict["listfolder"]
            method_params["auth"] = self.token
            method_params["folderid"] = folder_id
            method_params["recursive"] = 0

            url = self.regionUrl + "listfolder"
            res = requests.get(url, params=method_params)

        if res_obj := self.handle_status_code(res):
            res_obj = json.loads(res.text)
            result_code = res_obj["result"]

            if self.handle_result_code(result_code):
                return res_obj["metadata"]

    async def create_folder(self, folder_id="0", name=""):
        if self.valid_token() and folder_id and name:
            method_params = self.methodParamDict["createfolder"]
            method_params["auth"] = self.token
            method_params["folderid"] = folder_id
            method_params["name"] = name

            url = self.regionUrl + "createfolder"
            res = requests.get(url, params=method_params)

            if res_obj := self.handle_status_code(res):
                res_obj = json.loads(res.text)
                result_code = res_obj["result"]

                if self.handle_result_code(result_code):
                    return res_obj

    async def rename_folder(self, folder_id=None, toname=""):

        if self.valid_token() and folder_id and toname:
            method_params = self.methodParamDict["renamefolder"]
            method_params["auth"] = self.token
            method_params["folderid"] = folder_id
            method_params["toname"] = toname

            url = self.regionUrl + "renamefolder"
            res = requests.get(url, params=method_params)

            if res_obj := self.handle_status_code(res):
                res_obj = json.loads(res.text)
                result_code = res_obj["result"]

                if self.handle_result_code(result_code):
                    return res_obj

    async def delete_folder(self, folder_id="0"):
        if self.valid_token() and folder_id:
            method_params = self.methodParamDict["deletefolder"]
            method_params["auth"] = self.token
            method_params["folderid"] = folder_id

            url = self.regionUrl + "deletefolder"
            res = requests.get(url, params=method_params)
        pass



apic = PCloud()

apic.set_region("NA")
apic.set_username("hitujy@zetmail.com")
apic.set_password("test12345678")

print()
asyncio.run(apic.auth_digest())
print("Token: " + apic.token)
createdir = asyncio.run(apic.create_folder("0", "New Dir"))
print()
print()
filedir = asyncio.run(apic.list_folder("0"))
print("File Data: " + json.dumps(filedir, sort_keys=True, indent=4))
print()
print()

for item in filedir["contents"]:
    if item["name"] == "New Dir":
        asyncio.run(apic.rename_folder(item["folderid"], "Better Folder"))

filedir = asyncio.run(apic.list_folder("0"))
print("File Data: " + json.dumps(filedir, sort_keys=True, indent=4))

print()
print()
for item in filedir["contents"]:
    if item["name"] == "Better Folder":
        asyncio.run(apic.delete_folder(item["folderid"]))

filedir = asyncio.run(apic.list_folder("0"))
print("File Data: " + json.dumps(filedir, sort_keys=True, indent=4))
