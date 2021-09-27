import os
from RegUtil.data import *
from teste.data import *
from teste.funcTest import *
from tkinter.filedialog import *

testFile = []

if __name__ == '__main__':
	path = askdirectory()
	main = ""
	for path, dirs, files in os.walk(path):
		for file in files :
			if file != main+".java" and "." in file and not "Exception" in file:
				data = file.split('.')
				if data[1] == 'java':
					name = data[0]
					testFile.append(FunctionTest(path+separator+file,name[0]))

	print(testFile)
					

