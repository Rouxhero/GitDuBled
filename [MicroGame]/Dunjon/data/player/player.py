 #!/usr/bin/env python3
from util.Function import *
from map.Object import *

xImg = {-1:3,1:2,0:0}
yImg = {-1:1,1:0,0:0}
class Player:

	def __init__(self,pos,maps):
		self.stats = {

			"hp":100,
			"energie":100,
			"hit":2,
			"speed":2
		}
		self.dirs = (0,1)
		self.maps = maps
		self.size = maps.tileSize
		self.imgD = []
		for x in range(1,5):
			self.imgD.append(PyImgLoad('../img/player/player{}.png'.format(x),self.maps.tileSize))
		self.img = self.imgD[0]
		self.coord = pos


	def getPos(self):
		return self.coord.get()

	def move(self,x=0,y=0):
		speeds = self.stats['speed']
		self.dirs= (x,y)
		self.img = self.imgD[xImg[x]+yImg[y]]
		self.coord.move(x*speeds,y*speeds)
		stat = self.colide()
		if not stat  :
			self.coord.move(-x*speeds,-y*speeds)

	def colide(self):
		pos = self.coord.get()
		currentPos = Position(pos[0]//self.size[0],pos[1]//self.size[0])
		state =self.maps.containe(currentPos)
		currentPos = currentPos.get()
		tile = self.maps.mapGet(currentPos[0],currentPos[1])
		stateV =  tile.colide(self)
		tile = self.maps.mapGet(currentPos[0]+1,currentPos[1])
		stateV = stateV or tile.colide(self)
		tile = self.maps.mapGet(currentPos[0],currentPos[1]+1)
		stateV = stateV or tile.colide(self)
		return state and not stateV and True

	def show(self,display):
		pos = self.coord.get()
		display.blit(self.img,pos)

	def hit(self):
		currentPos = self.coord.get()
		target = self.maps.mapGet(currentPos[0]//self.size[0]+self.dirs[0],currentPos[1]//self.size[0]+self.dirs[1])
		target.hit(self.stats["hit"])



		



