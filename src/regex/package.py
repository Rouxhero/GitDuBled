# #!/usr/bin/env python3
# file for âckage class
from data import *
from joint import *
import os
class Package :

	def __init__(self,name,isSubPackge=True):
		self.name = name
		self.isSubPackge = isSubPackge
		self.classData = []

	def addClass(self,classO):
		self.classData.append(classO)


	def joint(self,joinData):
		JointCreator = Join(self.classData,joinData)


	def write(self,fatherRep,projectName):
		if not self.isSubPackge:
			os.system('mkdir {}/src/{}/{}'.format(fatherRep,projectName,self.name))

		

		for classO in self.classData:
		    head = "package "+projectName+"."+self.name+";"+line*3
		    if not self.isSubPackge:
		    	open(fatherRep+"/src/"+projectName+"/"+self.name+"/"+classO.flag['name']+".java","w").write(head+classO.toString())
		    else:	
		    	open(fatherRep+"/src/"+self.name+"/"+classO.flag['name']+".java","w").write(head+classO.toString())