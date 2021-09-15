from util.Function import *


class Game :

	def __init__(self,size):
		self.size = size
		pygame.init()
		self.display = pygame.display.set_mode(size)
		self.object = []
		self.play = True


	def over(self):
		self.play = False
 

	def show(self):
		for element in self.object:
			element.show(self.display)
