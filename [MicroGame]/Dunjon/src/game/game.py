#!/usr/bin/env python3
from util import *
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
			"clock":pygame.time.Clock()
		}
		self.font = {

			"load":pygame.font.SysFont('franklingothicmedium', 25),
			"text":pygame.font.SysFont('franklingothicmedium', 35)
		}
		self.pygameData['clock'].tick(self.getArg("tikspeed")[0])
		self.img = {}
		self.__loadImg()
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
				# pause(0.008)
				name = path+separator+file
				pack = name.split("img")[1].split('/')[1]
				self.pygameData['display'].blit(PyPrint("Loading img : {}".format(pack),(255,10,10),self.font['load']),(220,280))
				if pack in self.img :
					self.img[pack].append(PyImgLoad(name,self.getArg("TileSize")))
				else :
					self.img[pack] = [PyImgLoad(name,self.getArg("TileSize")),]
				self.pygameData['display'].blit(self.img[pack][-1],(280,320))
				pygame.display.update()



if __name__ == '__main__':
	game = Game()
	print(game.getArg("fullTile"))
	# game.setArg("Test",[150,150])
	print(game.getArg("Test"))
