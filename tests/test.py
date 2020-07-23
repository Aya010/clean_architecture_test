from methods.reader import Reader
from methods.txt_reader import TxtReader
from methods.csv_reader import CsvReader
from methods.zip_reader import ZipReader

ring_txt = []
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
