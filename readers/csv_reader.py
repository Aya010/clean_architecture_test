import csv  # python标准库

from entities.reader import Reader
from entities.person import Person

class CsvReader(Reader):  
    ext = '.csv'
    @classmethod
    def read(cls, file_path, people_list):
        with open(file_path, 'r') as csvfile:
            lines = csv.reader(csvfile, delimiter=' ')
            for line in lines:
                line_words = line[0].split(",")
                person_ = Person(line_words[0], eval(line_words[1]),
                                eval(line_words[2]))
                people_list.append(person_)
        return people_list
