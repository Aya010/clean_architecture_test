import os

from entities.reader import Reader
from entities.person import Person

class TxtReader(Reader):
    ext = ".txt"
    @classmethod
    def read(cls, file_path, people_list):
        with open(file_path) as txt_file:
            for line in txt_file:
                line_words = line.split(" ")
                person_ = Person(line_words[0], eval(
                    line_words[1]), eval(line_words[2]))
                people_list.append(person_)
        return people_list

    def __iter__(self, file_path):
        with open(file_path) as txt_file:
            for line in txt_file:
                line_words = line.split(" ")
                person_ = Person(line_words[0], eval(
                    line_words[1]), eval(line_words[2]))
                yield person_
