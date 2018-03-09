import csv

from typing import List, Any


class CSVReader(object):

    @staticmethod
    def read(filename: str) -> List[List[Any]]:
        with open(filename, 'r') as file:
            reader = csv.reader(file, delimiter=',')
            data: List[List[Any]] = []
            for row in reader:
                data.append(row)
            return data
