 #!/usr/bin/env python3
from util.Function import *
from util.Object import *


class Player:

 	def __init__(self,pos,maps):
 		self.stats = {

 			"hp":100,
 			"energie":100,
 			"speed":2
 		}
 		self.maps = maps
 		self.size = maps.tileSize
 		self.img = PyImgLoad('../img/player.png',self.maps.tileSize)
 		self.coord = pos


 	def getPos(self):
 		return self.coord.get()

 	def move(self,x=0,y=0):
 		speeds = self.stats['speed']
 		self.coord.move(x*speeds,y*speeds)
 		print("go")
 		stat = self.colide()
 		print(stat)
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
 		print(stateV)
 		return state and not stateV and True

 	def show(self,display):
 		pos = self.coord.get()
 		display.blit(self.img,pos)


 		



