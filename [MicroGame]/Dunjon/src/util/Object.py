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


	def colide(self,other):
		x = self.pos[0]
		y = self.pos[1]
		other_pos = other.coord.get()
		b_x = other_pos[0]
		b_y= other_pos[1]
		b_s = other.size[0]
		p1 = [max(x,b_x),max(y,b_y)]
		p2 = [min(x+20,b_x+b_s),min(y+20,b_y+b_s)]
		return (p1[0] < p2[0] and p1[1] < p2[1])



	def show(self,display):
		display.blit(self.img,self.pos)


class Wall(ObjectRPG):

	def __init__(self,coord:tuple,size:tuple,maps):
		super(Wall, self).__init__(coord,size,maps)
		self.str = "#"
		self.img = PyImgLoad('../img/Wall/wall1.png',size)


class Ground(ObjectRPG):


	def __init__(self,coord:tuple,size:tuple,maps):
		super(Ground, self).__init__(coord,size,maps)
		self.img = []
		self.str = " "
		for x in range(1,4):
			self.img.append(PyImgLoad('../img/ground/ground{}.png'.format(x),size))
		choix = r(0,100)
		if choix < 6:
			self.img = self.img[2]
		else :
			self.img = self.img[0]

	def colide(self,other):
		return False

class Tree(ObjectRPG) :
	

	def __init__(self,coord:tuple,size:tuple,maps):
		super(Tree, self).__init__(coord,size,maps)
		self.img = []

		self.str = "T"
		for x in range(1,3):
			self.img.append(PyImgLoad('../img/tree/tree{}.png'.format(x),size))
		self.img = self.img[0]


# Dir = [1..7]
class Water(ObjectRPG) :

	def __init__(self,coord:tuple,size:tuple,maps,dirs:int):
		super(Water, self).__init__(coord,size,maps)
		self.str = "W"
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
