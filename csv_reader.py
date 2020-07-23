import csv  # python标准库

from reader import Reader
from domain.person import Person

class CsvReader(Reader):  
    ext = '.csv'

    def read(self, people_list):
        with open(self._file_name, 'r') as csvfile:
            lines = csv.reader(csvfile, delimiter=' ')
            for line in lines:
                line_words = line[0].split(",")
                person_ = Person(line_words[0], eval(line_words[1]),
                                eval(line_words[2]))
                people_list.append(person_)
        return people_list

    def __iter__(self):
        with open(self._file_name) as csv_file:
            for line in csv_file:
                line_words = line.split(",")
                person_ = Person(line_words[0], eval(line_words[1]),
                                eval(line_words[2]))
                yield person_
