#!/usr/bin/env python3
from util import *
from map import *
import os
from time import sleep as pause
separator = '/'


class Game :

	def __init__(self):
		self.data = {
			"fullTile":"300x300",
			"screenTile":'30x30',
			"TileSize":"20x20",
			"screenSize":"600x600",
			"tikspeed":"30"
		}
		pygame.init()
		pygame.font.init()
		self.pygameData = {

			"display":pygame.display.set_mode(self.getArg("screenSize")),
			"clock":pygame.time.Clock(),
			"continu":True
		}
		self.font = {

			"load":pygame.font.SysFont('franklingothicmedium', 25),
			"text":pygame.font.SysFont('franklingothicmedium', 35)
		}
		self.pygameData['clock'].tick(self.getArg("tikspeed")[0])
		self.img = {}
		self.__loadImg()
		self.map = Map(self)
		# MEnu
		# Map

	def getArg(self,key):
		if key in self.data:
			return tuple(maps(self.data[key].split('x'),int))

	def setArg(self,key,data):
		self.data[key] = 'x'.join(maps(data,str))

	def __loadImg(self):
		for path, dirs, files in os.walk("../../img/"):
			for file in files:
				self.pygameData['display'].fill((6,6,6))
				# pause(0.08)
				name = path+separator+file
				pack = name.split("img")[1].split('/')[1]
				fileName = name.split("img")[1].split('/')[-1]
				self.pygameData['display'].blit(PyPrint("Loading img : {}".format(pack),(255,10,10),self.font['load']),(220,280))
				if pack in self.img :
					self.img[pack][fileName] = PyImgLoad(name,self.getArg("TileSize"))
				else :
					self.img[pack] = {}
					self.img[pack][fileName] = PyImgLoad(name,self.getArg("TileSize"))
				self.pygameData['display'].blit(self.img[pack][fileName],(280,320))
				pygame.display.update()
		print(self.img)
		
	def over(self):
		self.pygameData['continu'] = False



if __name__ == '__main__':
	game = Game()
	while game.pygameData['continu']:
		for event in pygame.event.get():
			# Close if the user quits the game
			if event.type == QUIT:
				game.over()
		game.map.show(game.pygameData["display"])
		pygame.display.update()

	# print(game.getArg("tikspeed"))
	# game.setArg("tikspeed",[60])
	# print(game.getArg("tikspeed"))
