from util.Function import * 			
from random import choice



class ObjectRPG :

	def __init__(self,coord:tuple,size:tuple,maps):
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
		self.img = self.img[0]

class Tree(ObjectRPG) :

	def __init__(self,coord:tuple,size:tuple,maps):
		super(Tree, self).__init__(coord,size,maps)
		self.img = []
		for x in range(1,3):
			self.img.append(PyImgLoad('../img/tree/tree{}.png'.format(x),size))
		self.img = self.img[0]

class Water(ObjectRPG) :

	def __init__(self,coord:tuple,size:tuple,maps,dirs:int):
		super(Water, self).__init__(coord,size,maps)
		self.img = PyImgLoad('../img/water/water{}.png'.format(dirs+1),size)

