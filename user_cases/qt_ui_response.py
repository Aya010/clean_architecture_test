import os
from entities.josephus import Josephus
from user_cases.user_read import UsedReader as Reader
from user_cases.qt_ui import QtUi


class QtResponse(QtUi):
    def click_run(self):
        try:
            ring = []
            ring = Reader.read(self._path, ring)
            joseph = Josephus(self._start, self._step, ring)
            self.info.clear()
            self.info.append("...Start...")
            self.info.append("")
            for i in joseph:
                self.get_person_info(i)
            self.info.append("...Success...")
        except:
            self.info.clear()
            self.info.append("Please check your input...")

    def selceted_path(self, text):
        current_path = os.getcwd()
        self._path = current_path + "/files/" + text

    def start_Changed(self, text):
        if text == "":
            text = "0"
        self._start = int(text)

    def step_Changed(self, text):
        if text == "":
            text = "1"
        self._step = int(text)

    def get_person_info(self, person):
        self.info.append("Name:" + person.name)
        self.info.append("Age:" + str(person.age))
        if person.gender == 0:
            self.info.append("Gender:Male")
        else:
            self.info.append("Gender:Female")
        self.info.append("")
