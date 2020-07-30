import os
from entities.josephus import Josephus
from readers.user_read import UsedReader as Reader

current_path = os.getcwd()
#file_path = current_path + "/files/josephus_list2.txt"
file_path = current_path + "/files/josephus_list2.txt"
ring = []
ring = Reader.read(file_path, ring)

START = int(input("Start num:"))
STEP = int(input("StEP num:"))
joseph = Josephus(START, STEP, ring)
for i in joseph:
    print(i)
