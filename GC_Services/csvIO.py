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

from PySide2.QtWidgets import QFileDialog


class CsvIO:

    def __init__(self):
        self.data = []

    def open_csv(self):
        asyncio.run(self.read_csv())

    async def read_csv(self):
        """open_csv
            Purpose:
                Opens and reads csv file into the data array attribute
            Parameters:
                self
            Returns:
                None

        """
        # Get file path and open file in read mode
        file_name = QFileDialog.getOpenFileName(self, "Open CSV Files", "c\\", 'CSV Format (*.csv)')
        filepath = file_name[0]
        csv_file = open(filepath, "r")

        # Grab first two lines as headers
        line = csv_file.readline().split(",")
        line.pop()
        self.headers.append(line)

        line = csv_file.readline().split(",")
        line.pop()
        self.headers.append(line)

        # Dump the rest into the data array
        while (line := csv_file.readline()) != "":
            row = line.replace("\n", "").split(",")
            self.data.append(row)

        csv_file.close()









