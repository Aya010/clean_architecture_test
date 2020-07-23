import os.path

class Reader:
    ext = None

    def __init__(self, file_name):
        self._file_name = file_name

    def read(self, people_list):
        suffix = os.path.splitext(self._file_name)[1]
        for x in Reader.__subclasses__():
            if suffix == x.ext:
                people_list = x.read(self, people_list)
        return people_list