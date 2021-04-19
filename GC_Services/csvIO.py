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


class CsvIo:
    def __init__(self):
        self.data = [[""]]

    def import_data(self, file_path="", log_data=False):
        asyncio.run(self.load(file_path))
        self.handler_headers()

        if log_data:
            self.log_data()

        return self.data

    async def load(self, file_path=""):
        file = open(file_path, "rt", encoding="utf8")
        file_data = csv.reader(file)

        for row in file_data:
            self.data.append(row)

        file.close()

    def handler_headers(self):
        if self.calc_prob() > .5:
            self.data.pop(0)

    def calc_prob(self):
        empty = 0
        total = len(self.data[0])

        for column in self.data[0]:
            if not column:
                empty += 1

        return empty / total

    def log_data(self):
        for row in self.data:
            print(row)


csv_handler = CsvIo()
csv_handler.import_data("../Asset-2.csv", True)
