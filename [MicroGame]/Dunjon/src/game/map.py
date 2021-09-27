#!/usr/bin/env python3
import numpy as np

# Class Map :


class Map :

	def __init__(self,father):
		self.father = father
		self.cover = np.zero(self.father.getArg("fullTile"))
		self.ground = np.zero(self.father.getArg("fullTile"))



	def show(self,display):
		for y in self.ground:
			for x in y :
				self.pygameData['display'].blit(
		for y in self.cover:
			for x in y :
				tile[x].show(display)
			