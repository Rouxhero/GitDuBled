from util.Function import *
from util.Object import *
from util.River import *
from random import randint as r
tileSize = (20,20)

def checkPos(maps,typeTile,x,y):
	# print("test for {} at {},{}".format(typeTile,x,y))
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
	return state and stateV and True


class Map :

	def __init__(self,size:float):
		self.width  = size[0]//tileSize[0]
		self.height = size[1]//tileSize[1]
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
			river = River(self,tileSize)
			while not river.ok:
				river = River(self,tileSize)
			river.validePos()
			self.element.append(river)
		for nb in range(r(15,20)):

			x = r(0,self.width-1)
			y = r(0,self.height-1)
			while not type(self.map[x][y]) == Ground:
				x = r(0,self.width-1)
				y = r(0,self.height-1)
			pos = Position(x,y)
			self.addTile(Tree(pos,tileSize,self),pos)
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
					self.addTile(Tree(pos,tileSize,self),pos)
					self.mapGet(x,y).show(display)
					pygame.display.update()
		
	def mapGet(self,x,y):
		return self.map[x][y]

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
				self.addTile(Ground(pos,tileSize,self),pos)

	



		# self.map[self.height-1][self.width-1] = Wall(((self.width-1)*tileSize[0],(self.height-1)*tileSize[1]),tileSize,self)
		# self.map[0][self.width-1] = Wall(((self.width-1)*tileSize[1],0),tileSize,self)




