from zipfile import ZipFile  # python标准库

from test.entities.test_reader import Reader
from test.entities.test_person import Person

class ZipReader(Reader):  # return a list
    ext = '.zip'
    @classmethod
    def read(cls, file_path, people_list):
        with ZipFile(file_path, 'r') as zip_reader:
            file_list = zip_reader.namelist()
            for file_ in file_list:
                read_file = zip_reader.read(file_).decode('UTF-8')
                read_lines = read_file.split('\r\n')
                for x in ZipReader.__subclasses__():
                    if file_[-4:] == x.ext:
                        person_read = x(read_lines)
                        people_list = person_read.read(people_list)
        assert people_list[0].age == 11
        assert people_list[9].age == 101
        assert people_list[10].age == 0

        return people_list

class ZipReaderTxt(ZipReader):
    ext = '.txt'
    def __init__(self, read_lines):
        self.read_lines = read_lines
    def read(self, people_list):
        for read_line in self.read_lines:
            read_word = read_line.split(' ')
            read_word = read_word[:3]
            if read_word != ['']:
                person_info = Person(read_word[0], eval(
                    read_word[1]), eval(read_word[2]))
                people_list.append(person_info)
        return people_list


class ZipReaderCsv(ZipReader):
    ext = '.csv'
    def __init__(self, read_lines):
        self.read_lines = read_lines
    def read(self, people_list):
        for read_line in self.read_lines:
            read_word = read_line.split(',')
            if read_word != ['']:
                person_info = Person(read_word[0], eval(read_word[1]), eval(read_word[2]))
                people_list.append(person_info)
        return people_list