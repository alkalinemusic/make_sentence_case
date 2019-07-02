import sys
import re
from tkinter import * 
import tkMessageBox
import tkFileDialog


root = Tk()
root.config(bg='gray14')

class SentenceCase(object):
	"""docstring for SentenceCase"""
	def __init__(self, master):
		self.master = master
		master.title = ("Make Sentence Case")
		

sentence = sys.argv[1]

rtn = re.split('([.!?] *)', sentence)

str_pieces = []

for each in rtn:
	str_pieces.append(each.capitalize())

print("\n\n\n")
print(''.join(str_pieces))



my_gui = SentenceCase(root)

root.mainloop()
