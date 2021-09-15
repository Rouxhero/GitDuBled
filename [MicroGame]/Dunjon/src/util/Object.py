from util.Function import * 			


class Wall :

	def __init__(self,coord:tuple,size:tuple):
		self.pos = coord
		self.size = size
		self.img = PyImgLoad('../img/wall.png',size)

	def show(self,display):
		display.blit(self.img,self.pos)