import os
from entities.josephus import Josephus
from user_cases.user_read import UsedReader as Reader
from user_cases.qt_ui import QtUi

class QtResponse(QtUi):
    
    def click_run(self):
        ring = []
        ring = Reader.read(self._path, ring)
        joseph = Josephus(self._start, self._step, ring)
        self.info.clear()
        self.info.append("...Start...")
        self.info.append("")
        for i in joseph:
            self.info.append("Name:" + i.name)
            self.info.append("Age:" + str(i.age))
            if i.gender == 0:
                self.info.append("Gender:Male")
            else:
                self.info.append("Gender:Female")
            self.info.append("")
        self.info.append("...Success...")
        
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
