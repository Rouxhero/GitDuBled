# #!/usr/bin/env python3
# file for âckage class
from RegUtil.data import *
from RegUtil.joint import *
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


	def write(self,fatherRep,projectName,path):
		if not self.isSubPackge:
			os.system('mkdir {}{}src{}{}'.format(path+separator,fatherRep+separator,separator+projectName+separator,self.name))

		

		for classO in self.classData:
		    
		    if not self.isSubPackge:
		    	head = "package "+projectName+"."+self.name+";"+line*3
		    	open(path+separator+fatherRep+"/src/"+projectName+"/"+self.name+"/"+classO.flag['name']+".java","w").write(head+classO.toString())
		    else:	
		    	head = "package "+projectName+";"+line*3
		    	open(path+separator+fatherRep+"/src/"+self.name+"/"+classO.flag['name']+".java","w").write(head+classO.toString())