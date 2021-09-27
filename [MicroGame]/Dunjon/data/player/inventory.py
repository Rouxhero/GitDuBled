# #!/usr/bin/env python3
from util.Function import *

class Inventory :

	def __init__(self,tileSize):
		self.inventory = list(list(0 for x in range(10)) for x in range(10))
		self.index = (0,0)
		self.content = {}
		self.img = PyImgLoad("../img/UI/slot.png",(tileSize[0]*2,tileSize[1]*2))


	def addItem(self,item,qdt):
		self.index[0] += 1
		if self.index[0] >= 10:
			self.index[1]+=1
			self.index = 0
		self.inventory[self.index[1]][self.index[0]].append(item.id)
		self.content[item.id] = [item,qdt,tuple(self.index)]

	def getItem(self,item):
		index = self.content[item.id][2]
		return self.inventory[index[1]][index[0]]