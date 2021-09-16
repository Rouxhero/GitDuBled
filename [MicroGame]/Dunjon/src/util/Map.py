from util.Function import *
from util.Object import *
from random import randint as r
tileSize = (20,20)

def checkPos(maps,typeTile,x,y):
	print("test for {} at {},{}".format(typeTile,x,y))
	state = type(maps[x][y]) == Ground
	stateV = False
	if x+1 < len(maps):
		stateV = stateV or type(maps[x+1][y]) == typeTile
		if x > 1 :
			stateV = stateV or  type(maps[x-1][y]) == typeTile
			if y+1 < len(maps[0]):
				stateV = stateV or  type(maps[x][y+1]) == typeTile
				if y > 1 :
					stateV = stateV or  type(maps[x][y-1]) == typeTile
	return state and stateV


class Map :

	def __init__(self,size:float):
		self.width  = size[0]//tileSize[0]
		self.height = size[1]//tileSize[1]
		self.size = size
		self.map = list(list(0 for x in range(self.height)) for x in range(self.width))
		self._generateMap()

	def addTile(self,tile,pos):
		self.map[pos[0]][pos[1]] = tile

	def _generateMap(self):
		for x in range(len(self.map)):
			for y in range(len(self.map[0])):
				self.addTile(Ground((x,y),tileSize,self),(x,y))


		for nb in range(r(15,20)):
			x = r(0,self.width-1)
			y = r(0,self.height-1)
			self.addTile(Tree((x,y),tileSize,self),(x,y))
			nbOther = r(15,20)
			ind = 0
			while ind < nbOther:
				x = r(0,self.width-1)
				y = r(0,self.height-1)
				if checkPos(self.map,Tree,x,y):
					ind += 1
					self.addTile(Tree((x,y),tileSize,self),(x,y))
		for x in range(r(1,2)):
			self.__generateRiver()
	def mapGet(self,x,y):
		return self.map[x][y]


	def __generateRiver(self):
		start =(r(1,self.width-1),self.height-1)
		self.addTile(Water(start,tileSize,self,1),start)
		start =(start[0]-1,self.height-1)
		self.addTile(Water(start,tileSize,self,0),start)
		while start[1] >0 :
			start =(start[0]+1,start[1]-1)
			self.addTile(Water(start,tileSize,self,1),start)
			start =(start[0]-1,start[1])
			self.addTile(Water(start,tileSize,self,0),start)

		# self.map[self.height-1][self.width-1] = Wall(((self.width-1)*tileSize[0],(self.height-1)*tileSize[1]),tileSize,self)
		# self.map[0][self.width-1] = Wall(((self.width-1)*tileSize[1],0),tileSize,self)




