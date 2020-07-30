
"""import os
from sys import path
current_path = os.getcwd()
path.append(current_path)

"""
from reader import Reader
from txt_reader import TxtReader
from csv_reader import CsvReader
from zip_reader import ZipReader

strl = os.getcwd()
list1 = [strl, "hello"]
print(list1)
 
list1.append( strl + "\\rest\\josephus_list2.txt")
print(list1)

"""ring_txt = []
func = Reader("josephus_list2.txt")
ring_txt = func.read(ring_txt)
assert(ring_txt[0].get_age() == 11)

ring_csv = []
func = Reader("josephus_list1.csv")
ring_csv = func.read(ring_csv)
assert(ring_csv[0].get_age() == 0)

ring_zip = []
func = Reader("josephus.zip")
ring_zip = func.read(ring_zip)
assert(ring_zip[0].get_age() == 11)
"""