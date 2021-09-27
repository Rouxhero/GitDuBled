from util.Function import *
from map.Map import *
from player.player import *
class Game :

	def __init__(self,size):
		self.size = size
		self.actualMap = Map(size)
		pygame.init()
		self.display = pygame.display.set_mode(size,True)
		self.actualMap.generateMap(self.display)
		self.player = Player(Position(30,30),self.actualMap)
		self.object = []
		self.play = True
		for y in range(len(self.actualMap.map)):
			for x in range(len(self.actualMap.map[y])):
				print(self.actualMap.mapGet(x,y).str,end="|")
			print('\n','-'*(len(self.actualMap.map)*2))


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
		self.player.show(self.display)
