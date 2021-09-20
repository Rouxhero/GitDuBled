from util.Function import * 			
from random import choice
from random import randint as r



class ObjectRPG :

	def __init__(self,coord,size:tuple,maps):
		self.coord = coord
		coord = coord.get()
		self.pos = (coord[0]*size[0],coord[1]*size[1])
		self.size = size
		self.maps = maps


	def show(self,display):
		display.blit(self.img,self.pos)


class Wall(ObjectRPG):

	def __init__(self,coord:tuple,size:tuple,maps):
		super(Wall, self).__init__(coord,size,maps)
		self.img = PyImgLoad('../img/Wall/wall1.png',size)


class Ground(ObjectRPG):


	def __init__(self,coord:tuple,size:tuple,maps):
		super(Ground, self).__init__(coord,size,maps)
		self.img = []
		for x in range(1,4):
			self.img.append(PyImgLoad('../img/ground/ground{}.png'.format(x),size))
		choix = r(0,100)
		if choix > 97:
			self.img = self.img[1]
		elif choix < 6:
			self.img = self.img[2]
		else :
			self.img = self.img[0]

class Tree(ObjectRPG) :

	def __init__(self,coord:tuple,size:tuple,maps):
		super(Tree, self).__init__(coord,size,maps)
		self.img = []
		for x in range(1,3):
			self.img.append(PyImgLoad('../img/tree/tree{}.png'.format(x),size))
		self.img = self.img[0]


# Dir = [1..7]
class Water(ObjectRPG) :

	def __init__(self,coord:tuple,size:tuple,maps,dirs:int):
		super(Water, self).__init__(coord,size,maps)
		self.img = PyImgLoad('../img/water/water{}.png'.format(dirs+1),size)



class Position :

	def __init__(self,x,y):
		self.x = x
		self.y = y

	def move(self,x=0,y=0):
		self.x += x
		self.y += y

	def copy(self):
		return Position(self.x,self.y)

	def get(self):
		return (self.x,self.y)
