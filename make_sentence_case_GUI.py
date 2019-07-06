import sys
import re
import tkinter as tk
# import tkMessageBox
# import tkFileDialog


root = tk.Tk()
root.config(bg='gray14')

class SentenceCase:
	"""docstring for SentenceCase"""
	def __init__(self, master):
		# super(SentenceCase, self).__init__()
		self.master = master
		master.title("Make Sentence Case")

		sentence_text = tk.StringVar()
		self.text_entry = tk.Entry(master, textvariable=sentence_text)
		self.text_entry.config(fg='bisque1', bg='gray28', font='bold')
		text_entry_label = tk.Label(root, text="Enter sentence/paragraph here", font='bold')
		text_entry_label.config(fg='bisque3', bg='gray14')
		text_entry_label.grid(row=1, column=0, sticky=tk.W)								



		self.text_entry.grid(row=1, column=1, columnspan=40, sticky=tk.W+tk.E)	

		def sentence_conversion(*args):
			print(sentence_text.get())
			# sentence = self.text_entry
			# rtn = re.split('([.!?] *)', sentence)
			# str_pieces = []
			# for each in rtn:
			# 	str_pieces.append(each.capitalize())


			# sentence = sys.argv[1]

			# rtn = re.split('([.!?] *)', sentence)

			# str_pieces = []

			# for each in rtn:
			# 	str_pieces.append(each.capitalize())

			# print("\n\n\n")
			# print(''.join(str_pieces))

		self.convert_button = tk.Button(master, text="Convert", fg='bisque1',bg='gray28',
								 font='bold', command=sentence_conversion)
		self.convert_button.grid(row=2, column=0, sticky=tk.W)
	

my_gui = SentenceCase(root)

root.mainloop()
