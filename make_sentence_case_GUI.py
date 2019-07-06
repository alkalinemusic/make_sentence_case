import sys
import re
from tkinter import * 
# import tkMessageBox
# import tkFileDialog


root = Tk()
root.config(bg='gray14')

class SentenceCase:
	"""docstring for SentenceCase"""
	def __init__(self, master):
		super(SentenceCase, self).__init__()
		self.master = master
		master.title("Make Sentence Case")

	sentence_text = StringVar()
	self.text_entry = Entry(master, textvariable=sentence_text)
	self.text_entry.config(fg='bisque1', bg='gray28', font='bold')
	text_entry_label = Label(root, text="Enter sentence/paragraph here", font='bold')
	text_entry_label.config(fg='bisque3', bg='gray14')
	text_entry_label.grid(row=1, column=0, sticky=W)								


	self.projectNameEntry.grid(row=1, column=1, columnspan=40, sticky=W+E)	

	def sentence_conversion():
		pass
		# sentence = sys.argv[1]

		# rtn = re.split('([.!?] *)', sentence)

		# str_pieces = []

		# for each in rtn:
		# 	str_pieces.append(each.capitalize())

		# print("\n\n\n")
		# print(''.join(str_pieces))

	

my_gui = SentenceCase(root)

root.mainloop()
