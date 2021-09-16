from util.Function import *
from util.Object import *
from random import randint as r
tileSize = (20,20)


def checkPos(maps,typeTile,x,y):
	return type(maps[y][x]) == Ground and (
					type(maps[y+1][x]) == typeTile
					or  type(maps[y-1][x]) == typeTile
					or  type(maps[y][x+1]) == typeTile
					or  type(maps[y][x-1]) == typeTile
				)
class Map :

	def __init__(self,size:float):
		self.width  = size[0]//tileSize[0]
		self.height = size[1]//tileSize[1]
		self.size = size
		self.map = list(list(0 for x in range(self.width)) for x in range(self.height))
		self._generateMap()

	def addTile(self,tile,pos):
		self.map[pos[1]][pos[0]] = tile

	def _generateMap(self):
		for x in range(len(self.map)):
			for y in range(len(self.map[0])):
				pos = (y*tileSize[0] ,x*tileSize[1])
				self.addTile(Ground(pos,tileSize,self),(y,x))


		for nb in range(r(6,12)):
			x = r(2,self.width-2)
			y = r(2,self.height-2)
			pos = (x*tileSize[1],y*tileSize[0])
			self.addTile(Tree(pos,tileSize,self),(x,y))
			nbOther = r(10,20)
			ind = 0
			while ind < nbOther:
				x = r(2,self.width-2)
				y = r(2,self.height-2)
				if checkPos(self.map,Tree,x,y):
					ind += 1
					pos = (x*tileSize[1],y*tileSize[0])
					self.addTile(Tree(pos,tileSize,self),(x,y))
		for x in range(r(1,2)):
			self.__generateRiver()


	def __generateRiver(self):
		start =(self.width-tileSize[0], r(2,self.height))
		pos = (start[1]*tileSize[1],start[0]*tileSize[0])
		self.addTile(Water(pos,tileSize,self),start )
		# self.map[self.height-1][self.width-1] = Wall(((self.width-1)*tileSize[0],(self.height-1)*tileSize[1]),tileSize,self)
		# self.map[0][self.width-1] = Wall(((self.width-1)*tileSize[1],0),tileSize,self)




