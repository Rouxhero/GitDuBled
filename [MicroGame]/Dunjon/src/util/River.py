from util.Function import *
from util.Object import *
from random import randint as r
class River :

	def __init__(self,maps,tileSize):
		self.maps = maps
		self.tileSize = tileSize
		self.element = []
		self.__generateRiver()



	def __checkPos(self,pos,size,dirs=1):
		# dir : -1 => LEFT 1 => RIGHT
		pos.move(NONE,UP)
		if self.maps.containe(pos) :
			pos.move(size*dirs)
			print('ok for First pos')
			if self.maps.containe(pos) :
				pos.move(-size*dirs)
				print('ok for second pos')
				print(type(self.maps.mapGetT(self.start)))
				if type(self.maps.mapGetT(self.start)) == Ground :
					pos.move(NONE,DOWN)
					return True
		pos.move(NONE,DOWN)
		return False



	def __foward(self):

		self.start.move(RIGHT,UP)
		self.__AddTile(self.start,1)
		self.start.move(LEFT)
		self.__AddTile(self.start,0)

	def __left(self):
		self.start.move(RIGHT)
		self.__AddTile(self.start,4)
		self.start.move(LEFT)
		self.__AddTile(self.start,2)
		self.start.move(LEFT)
		self.__AddTile(self.start,5)
		self.__foward()

	def __right(self):
		self.__AddTile(self.start,3)
		self.start.move(RIGHT)
		self.__AddTile(self.start,2)
		self.start.move(RIGHT)
		self.__AddTile(self.start,6)
		self.start.move(NONE,UP)
		self.__AddTile(self.start,1)
		self.start.move(LEFT)
		self.__AddTile(self.start,0)

	def __AddTile(self,pos,key=1):
		water = Water(pos,self.tileSize,self,key)
		self.element.append(water)
		self.maps.addTile(water,pos)

	def __generateRiver(self):
		self.start =Position(r(1,self.maps.width-1),self.maps.height-1)	
		# Move For the first foward
		if self.__checkPos(self.start,1) :
			self.start.move(NONE,DOWN)
			self.__foward()
		while self.start.get()[1] > 0 :
			# import ipdb; ipdb.set_trace()
			# state : 1 = | | 2 = <- 3 = ->
			choix = r(0,100)
			print(self.start.get(),choix)
			if choix < 50 :
				if self.__checkPos(self.start,1):
					self.__foward()	
			else :
				dirs = r(0,1)
				if dirs == 1 :
					if self.__checkPos(self.start,2,LEFT):
						self.__left()	
				else :
					if self.__checkPos(self.start,2,RIGHT):
						self.__right()	


						

    
    