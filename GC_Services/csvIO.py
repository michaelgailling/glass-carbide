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


import asyncio
import csv
from PySide2.QtWidgets import QFileDialog


class CsvIo:
    def __init__(self):
        self.data = [[""]]

    def import_data(self, file_path="", log_data=False):
        self.load(file_path)
        self.handler_headers()
        if log_data:
            self.log_data()
        return self.data

    def load(self, file_path=""):
        file = open(file_path, "rt", encoding="utf8")
        file_data = csv.reader(file)

        for row in file_data:
            self.data.append(row)

        self.handler_headers()

        file.close()

    def handler_headers(self):
        empty = 0
        total = len(self.data[0])

        for column in self.data[0]:
            if not column:
                empty += 1

        probability = empty/total

        if probability > .5:
            self.data.pop(0)

    def log_data(self):
        for row in self.data:
            print(row)


csv_handler = CsvIo()
csv_handler.import_data("../Asset-2.csv", True)
