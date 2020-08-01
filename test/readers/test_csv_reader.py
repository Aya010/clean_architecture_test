import csv  # python标准库

from test.entities.test_reader import Reader
from test.entities.test_person import Person

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
        assert people_list[0].age == 0
        assert people_list[12].age == 12
        return people_list
