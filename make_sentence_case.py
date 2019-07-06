import sys
import re

sentence = sys.argv[1]

rtn = re.split('([.!?] *)', sentence)

str_pieces = []

for each in rtn:
	str_pieces.append(each.capitalize())

print("\n\n\n")
print(''.join(str_pieces))
