# #!/usr/bin/env python3
from teste.data import *
import re


class FunctionTest :

	def __init__(self,file,name):
		self.file = file
		self.name = name
		self.code = ""
		self.__uncodeFile()


	def __uncodeFile(self):
		# open file
		theFile = open(self.file,"r")
		print(self.file)
		# GET PACK
		line = theFile.readline()
		self.code += head(line,self.name)
		# GET ALL FUNC
		
		while line :
			if re.match(funcR,line):
				print(line)
			line = theFile.readline()

