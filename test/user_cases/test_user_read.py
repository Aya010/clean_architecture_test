import os
from test.entities.test_reader import Reader
from test.readers.test_txt_reader import TxtReader
from test.readers.test_csv_reader import CsvReader
from test.readers.test_zip_reader import ZipReader

class UsedReader:
    ext = None
    @classmethod
    def read(cls, file_path, people_list):
        suffix = os.path.splitext(file_path)[1]
        for x in Reader.__subclasses__():
            if suffix == x.ext:
                people_list = x.read(file_path, people_list)
        return people_list
        
