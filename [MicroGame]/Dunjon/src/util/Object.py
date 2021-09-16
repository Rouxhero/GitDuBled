from util.Function import * 			


class Wall :

	def __init__(self,coord:tuple,size:tuple,map):
		self.pos = coord
		self.size = size
		if coord == (0,0):
			self.img = PyImgLoad('../img/Wall/wall2.png',size)
		else :
			self.img = PyImgLoad('../img/Wall/wall1.png',size)

	def show(self,display):
		display.blit(self.img,self.pos)


class Ground :

	def __init__(self,coord:tuple,size:tuple,map):
		self.pos = coord
		self.size = size
		self.img = []
		for x in range(1,4):
			self.img.append(PyImgLoad('../img/ground/ground{}.png'.format(x),size))

	def show(self,display):
		display.blit(self.img[0],self.pos)


class Tree :

	def __init__(self,coord:tuple,size:tuple,map):
		self.pos = coord
		self.size = size
		self.img = []
		for x in range(1,3):
			self.img.append(PyImgLoad('../img/tree/tree{}.png'.format(x),size))




	def show(self,display):
		display.blit(self.img[0],self.pos)



class Water :

	def __init__(self,coord:tuple,size:tuple,map,dirs:int):
		self.pos = coord
		self.size = size
		self.img = []
		for x in range(1,3):
			self.img.append(PyImgLoad('../img/tree/tree{}.png'.format(x),size))
		self.dir = dirs




	def show(self,display):
		display.blit(self.img[self.dir],self.pos)