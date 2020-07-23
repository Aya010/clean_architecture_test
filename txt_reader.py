
from reader import Reader
from domain.person import Person

class TxtReader(Reader):
    ext = ".txt"

    def read(self, people_list):
        with open(self._file_name) as txt_file:
            for line in txt_file:
                line_words = line.split(" ")
                person_ = Person(line_words[0], eval(
                    line_words[1]), eval(line_words[2]))
                people_list.append(person_)
        return people_list

    def __iter__(self):
        with open(self._file_name) as txt_file:
            for line in txt_file:
                line_words = line.split(" ")
                person_ = Person(line_words[0], eval(
                    line_words[1]), eval(line_words[2]))
                yield person_
