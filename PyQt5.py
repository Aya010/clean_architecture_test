# -*- coding: utf-8 -*-
 
import os
import sys
from PyQt5.QtWidgets import (QComboBox, QWidget, QLabel, QTextBrowser,
                             QLineEdit, QApplication, QPushButton)
from entities.josephus import Josephus
from readers.user_read import UsedReader as Reader

class QtUi(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.input_start()
        self.input_step()
        self.select_path()
        self.run_button()
        self.out_info()
        self.setGeometry(300, 300, 350, 340)
        self.setWindowTitle('Josephus Ring')
        self.show()

    def input_start(self):
        qtlabel = QLabel(self)
        start = QLineEdit(self)
        start.setPlaceholderText("请输入0~3位数字")
        qtlabel.move(20, 40)
        qtlabel.setText("Start:")
        start.move(60, 35)
        start.textChanged[str].connect(self.start_Changed)
        start.adjustSize()

    def input_step(self):
        qtlabel = QLabel(self)
        step = QLineEdit(self)
        step.setPlaceholderText("请输入0~3位数字")
        qtlabel.move(20, 70)
        qtlabel.setText("Step:")
        step.move(60, 65)
        step.textChanged[str].connect(self.step_Changed)
        step.adjustSize()

    def select_path(self):
        path_label = QLabel(self)
        path = QComboBox(self)
        path_label.move(20, 100)
        path_label.setText("File:")
        path.addItem("josephus_list1.csv")
        path.addItem("josephus_list2.txt")
        path.addItem("josephus.zip")
        path.move(60, 95)
        path.activated[str].connect(self.selceted_path)

    def run_button(self):
        run = QPushButton('RUN', self)
        run.move(150, 138)
        run.clicked.connect(self.click_run)
        run.adjustSize()

    def out_info(self):
        self.info = QTextBrowser(self)
        self.info.move(30,180)
        self.info.resize(290,150)

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
        #print(self._start)
        #self.start.adjustSize()

    def step_Changed(self, text):
        if text == "":
            text = "1"
        self._step = int(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = QtUi()
    sys.exit(app.exec_())
