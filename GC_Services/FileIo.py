import asyncio
import json

from pcloudAPI import PCloud


class FileIo:
    def __init__(self):
        project_dir = ""

    def save_file_to_dir(self, filename, file_bytes):
        open(self.project_dir + "/" + filename, "wb").write(file_bytes)


fio = FileIo()

fio.project_dir = "C:/Work/Outrageous/FileDump"

apic = PCloud()

apic.set_region("NA")
pub_link_dir = asyncio.run(apic.show_pub_link_directory("kZXpOjXZnGCxvIiKSzJbuYQUiakTARUrXj7V"))

pub_link_download = asyncio.run(apic.get_pub_link_download(code="kZXpOjXZnGCxvIiKSzJbuYQUiakTARUrXj7V", file_id="27739405968"))

host = "http://" + pub_link_download["hosts"][0]
path = pub_link_download["path"]

url = host + path

file_res = asyncio.run(apic.download_file(url))

fio.save_file_to_dir("TEST.jpg", file_res)

