"""
There are class and function about Josephus Problem.
"""
import copy

class Josephus:
    def __init__(self, start, step, people):
        self._people = people
        self.start = start 
        self._current = self.start - 1
        self.step = step

    def __iter__(self): 
        self._iter = copy.deepcopy(self._people)
        current = self.start - 1
        while len(self._iter) > 0:
            current =  self._get_pop_order(self._iter, current)
            yield self._iter.pop(current)

    def append(self, person):
        self._people.append(person)

    def pop(self):
        self._current = self._get_pop_order(self._people, self._current)
        return self._people.pop(self._current)

    def _get_pop_order(self, target, current):
        num = len(target)
        current = (current + self.step - 1) % num
        return current