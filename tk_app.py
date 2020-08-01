#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *

import os
from entities.josephus import Josephus
from user_cases.user_read import UsedReader as Reader

file_list = ["josephus_list1.csv",
             "josephus_list2.txt", "josephus.zip"]

class TkGui():
    def __init__(self,top_window):
        self.top_window = top_window


    #设置窗口
    def set_joseph_window(self):
        self.top_window.title("Josephuse Ring")           #窗口名
        self.top_window.geometry('460x520+10+10')     
        #标签
        self.in_start_label = Label(self.top_window, text="起始序号:")
        self.in_start_label.grid(row=1, column=0)
        self.in_step_label = Label(self.top_window, text="间隔人数:")
        self.in_step_label.grid(row=1, column=3)
        self.log_label = Label(self.top_window, text="约瑟夫环序列")
        self.log_label.grid(row=12, column=2)
        self.path_label = Label(self.top_window, text="请选择文件")
        self.path_label.grid(row=3, column=0)
        #文本框
        self.in_start_Text = Text(self.top_window, width=10, height=1)  #原始数据录入框
        self.in_start_Text.grid(row=1, column=2)
        self.in_step_Text = Text(self.top_window, width=10, height=1)
        self.in_step_Text.grid(row=1, column=4)
        self.out_text = Text(self.top_window, width=66, height=20)
        self.out_text.grid(row=13, column=0, columnspan=10)
        #LIstbox
        self.path = Listbox(self.top_window)
        self.path.grid(row=3, column=2)
        for i in file_list:
            self.path.insert(END, i)

        #按钮
        self.run_button = Button(self.top_window, text="RUN", bg="lightblue", width=10,command=self.joseph_output)  # 调用内部方法  加()为直接调用
        self.run_button.grid(row=3, column=4)


    #功能函数
    def joseph_output(self):
        self.out_text.delete(1.0, END)
        file_order = self.path.curselection()
        #print(file_order)
        if file_order:
            try:
                current_path = os.getcwd()
                file_name = file_list[file_order[0]]
                file_path = "/".join([current_path, "files", file_name])
                ring = []
                ring = Reader.read(file_path, ring)
                START = int(self.in_start_Text.get(1.0,END))
                STEP = int(self.in_step_Text.get(1.0,END))
                joseph = Josephus(START, STEP, ring)
                for i in joseph:
                    self.read_person(i)
            except:
                self.out_text.insert(END, "Please check up the start and step numbers are legal")
        else:
            self.out_text.insert(END, "Please select a file...")
            

    def read_person(self, person):
        self.out_text.insert(END,"Name:" + person.name + "\n")
        self.out_text.insert(END,"Age:" + str(person.age) + "\n")
        if person.gender == 0:
            self.out_text.insert(END,"Gender:Male" + "\n")
        else:
            self.out_text.insert(END,"Gender:Female" + "\n")
        self.out_text.insert(END, "\n")

if __name__ == '__main__':
    tk_window = Tk() 
    joseph_window = TkGui(tk_window)
    joseph_window.set_joseph_window()
    tk_window.mainloop() 
