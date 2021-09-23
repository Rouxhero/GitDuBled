from util.Function import *
from map.Function import *
from map.Object import *
from map.River import *
from random import randint as r




class Map :

	def __init__(self,size:float):
		self.size = (30,30) # Number of tiles in the display
		self.fullSize = (300,300)
		self.displaySize = size
		self.centerPos = Position(150,150)
		self.tileSize = (size[0]//self.size[0],size[1]//self.size[0])
		self.ground = []
		self.cover  = []

	def contain(self,pos):
		pos = pos.get()
		states = True
		for coord in range(len(pos)) :
			states =  states and pos[coord] >= 0 and pos[coord] < self.fullSize[coord]
		return states


	def addTile(self,tile,pos):
		pos = pos.get()
		try :
			self.map[pos[0]][pos[1]] = tile
			return True
		except Exception as e:
			print(e)
			return False


	def __generateRiver(self):
		for x in range(r(1,2)):
			river = River(self,self.tileSize)
			while not river.ok:
				river = River(self,self.tileSize)
			river.validePos()
			self.ground.append(river)

	def __generateTree(self):
		for nb in range(r(15,20)):
			x = r(0,self.fullSize[0]-1)
			y = r(0,self.fullSize[1]-1)
			while not type(self.map[x][y]) == Ground:
				x = r(0,self.fullSize[0]-1)
				y = r(0,self.fullSize[1]-1)
			pos = Position(x,y)
			self.addTile(Tree(pos,self.tileSize,self),pos)
			self.mapGet(x,y).show(display)
			pygame.display.update()
			nbOther = r(15,20)
			ind = 0
			while ind < nbOther:
				x = r(0,self.fullSize[0]-1)
				y = r(0,self.fullSize[1]-1)
				if checkPos(self.map,Tree,x,y):
					ind += 1
					pos = Position(x,y)
					self.addTile(Tree(pos,self.tileSize,self),pos)
					self.mapGet(x,y).show(display)
					pygame.display.update()