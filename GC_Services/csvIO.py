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
    """CSV IO

                Summary:
                    A class for {Type} that includes:

                    -{Description} to the {Location eg left}

                Attributes:
                    self

                Methods:
                    import_data, load, handler_headers, calc_prob, trim_columns, log_data

                Attributes
                ----------
                    self

                Methods
                -------
                    import_data(self, file_path="", handle_header=True, log_data=False)
                        Returns CSV data
                    load(self, file_path="")
                        Opens CSV and loads data
                    handler_headers(self)
                        !!! Processes headers !!!
                    calc_prob(self)
                        Returns percentage of empty cells in row
                    trim_columns(self)
                        Trims columns from data
                    log_data(self)
                        Prints out contents of data
            """
    def __init__(self):
        """Constructor:
            Initialize CSV parsing service

            Parameters:
                self
            Returns:
                None
        """
        self.data = []

    def import_data(self, file_path="", handle_header=True, log_data=False):
        asyncio.run(self.load(file_path))

        if handle_header:
            self.handler_headers()

        self.trim_columns()

        if log_data:
            self.log_data()

        return self.data

    async def load(self, file_path=""):
        try:
            file = open(file_path, "rt", encoding="utf8")
            file_data = csv.reader(file)

            for row in file_data:
                self.data.append(row)

            file.close()
        except PermissionError:
            pass

    def handler_headers(self):
        if self.calc_prob() > 0.2:
            self.data.pop(0)

    def calc_prob(self):
        empty = 0
        total = len(self.data[0])

        for column in self.data[0]:
            if not column:
                empty += 1

        return empty / total

    def trim_columns(self):
        temp_data = self.data

        for column in range(0, len(temp_data[0])):

            if not temp_data[0][column]:

                for row in self.data:
                    row.pop(column)

    def log_data(self):
        for row in self.data:
            print(row)



