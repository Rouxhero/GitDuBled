from util.Function import *
from util.Map import *

class Game :

	def __init__(self,size):
		self.size = size
		self.actualMap = Map(size)
		pygame.init()
		self.display = pygame.display.set_mode(size)
		self.actualMap.generateMap(self.display)
		self.object = []
		self.play = True


	def over(self):
		self.play = False
 

	def reloadMap(self):
 		self.actualMap = Map(self.size)
 		self.display.fill((0,0,0))
 		self.actualMap.generateMap(self.display)

	def show(self):
		for y in self.actualMap.map:
			for x in y:
				x.show(self.display)
