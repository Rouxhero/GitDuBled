import os
from RegUtil.data import *
from teste.data import *
from tkinter.filedialog import *

if __name__ == '__main__':
	path = askdirectory()
	main = ""
	for path, dirs, files in os.walk(path):
		for file in files :
			print(path+separator+file)
			if file != main+".java" and "." in file:
				data = file.split('.')
				if data[1] == 'java':
					name = data[0]
					package = open(path+separator+file,"r").readline()
					print(head(package,name))

