#!/usr/bin/env python3
import numpy as np
from tileData import *
# Class Map :


class Map :

	def __init__(self,father):
		self.father = father
		self.cover = np.zeros(self.father.getArg("fullTile"))
		self.ground = np.zeros(self.father.getArg("fullTile"))



	def show(self,display):
<<<<<<< HEAD
		for y in self.ground:
			for x in y :
				self.pygameData['display'].blit(
		for y in self.cover:
			for x in y :
				tile[x].show(display)
			
=======
		for y in range(len(self.ground)):
			for x in range(len(self.ground[y])) :
				data = tileData[self.ground[y][x]]
				display.blit(self.father.img[data["pack"]][data["file"]],(x*20,y*20))

		# for y in self.cover:
		# 	for x in y :
		# 		tile[x].show(display)
		# 	
>>>>>>> 9ea69cdf406f1785d5f213408c6627a2838e6240
