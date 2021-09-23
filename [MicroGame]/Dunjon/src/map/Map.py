from util.Function import *
from map.Object import *
from map.River import *
from random import randint as r





class Map :

	def __init__(self,size:float):
		self.width  = 30
		self.height = 30
		self.tileSize = (size[0]//30,size[1]//30)
		print(self.tileSize,self.height)
		self.size = size
		self.element = []
		self.map = list(list(0 for x in range(self.height)) for y in range(self.width))


	def containe(self,pos):
		pos = pos.get()
		return pos[0] >= 0 and pos[0] < self.width and pos[1] >= 0 and pos[1] < self.height
		
	def addTile(self,tile,pos):
		pos = pos.get()
		self.map[pos[0]][pos[1]] = tile

	def generateMap(self,display):
		
		self.generateGround()
		pygame.display.update()

		for x in range(r(1,2)):
			river = River(self,self.tileSize)
			while not river.ok:
				river = River(self,self.tileSize)
			river.validePos()
			self.element.append(river)
		for nb in range(r(15,20)):

			x = r(0,self.width-1)
			y = r(0,self.height-1)
			while not type(self.map[x][y]) == Ground:
				x = r(0,self.width-1)
				y = r(0,self.height-1)
			pos = Position(x,y)
			self.addTile(Tree(pos,self.tileSize,self),pos)
			self.mapGet(x,y).show(display)
			pygame.display.update()
			nbOther = r(15,20)
			ind = 0
			while ind < nbOther:
				x = r(0,self.width-1)
				y = r(0,self.height-1)
				if checkPos(self.map,Tree,x,y):
					ind += 1
					pos = Position(x,y)
					self.addTile(Tree(pos,self.tileSize,self),pos)
					self.mapGet(x,y).show(display)
					pygame.display.update()
		for x in range(4):
			for y in range(4):
				pos = Position(x,y)
				self.addTile(Ground(pos,self.tileSize,self),pos)
		
	def mapGet(self,x,y):
		try :
			return self.map[x][y]
		except Exception as e:
			print(x,y,e)
			return False

	def mapGetT(self,pos):
		try :
			pos = pos.get()
			return self.map[pos[0]][pos[1]]
		except Exception as e:
			print(e)
			return False

	def generateGround(self):
		for x in range(len(self.map)):
			for y in range(len(self.map[0])):
				pos = Position(x,y)
				self.addTile(Ground(pos,self.tileSize,self),pos)

	



		# self.map[self.height-1][self.width-1] = Wall(((self.width-1)*tileSize[0],(self.height-1)*tileSize[1]),tileSize,self)
		# self.map[0][self.width-1] = Wall(((self.width-1)*tileSize[1],0),tileSize,self)




