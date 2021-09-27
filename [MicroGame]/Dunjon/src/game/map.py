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
		for y in range(len(self.ground)):
			for x in range(len(self.ground[y])) :
				data = tileData[self.ground[y][x]]
				display.blit(self.father.img[data["pack"]][data["file"]],(x*20,y*20))

		# for y in self.cover:
		# 	for x in y :
		# 		tile[x].show(display)
		# 	