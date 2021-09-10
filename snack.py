import pygame
from pygame.locals import *
from random import randint as r
from random import choice
from time import sleep as pause
#Game var

SPEED = 22
TICK = 7
BONUS_SPAWN = lambda :((TICK%5)+1)*10
# Size of bonus
LITTLE = (5,5)
MIDLLE = (7,7)
BIG    = (10,10)
sizeList = (LITTLE,MIDLLE,BIG)

# Color of element
BONUS_1   = (255,0,0)
BONUS_2  = (0,0,255)
BONUS_COLOR = [BONUS_1,BONUS_2]

SNACK = (3,255,55)

bonus_state = 0
bonus = []


class Snack :

	def __init__(self):
		self.score = 0
		self.square = pygame.Surface((20,20))
		self.key = (1,0)
		self.square.fill(SNACK)
		self.size = 3
		self.pos = [(200,200),(222,200),(244,200)]

	def show(self,surface):
		for pos in range(self.size):
			surface.blit(self.square,self.pos[pos])

	def move(self):
		old = ()
		temp = ()
		for pos in range(0,self.size):
			if pos == 0:
				old = self.pos[pos]
				self.pos[pos] = (self.pos[pos][0] + self.key[0]*SPEED,self.pos[pos][1] + self.key[1]*SPEED)
			else :
				temp = self.pos[pos]
				self.pos[pos] = old
				old = temp
	def colide(self,bonus,TICK):
		x = self.pos[0][0]
		y = self.pos[0][1]
		for bonu in bonus:
			b_x = bonu.pos[0]
			b_y= bonu.pos[1]
			b_s = bonu.size[0]
			p1 = [max(x,b_x),max(y,b_y)]
			p2 = [min(x+20,b_x+b_s),min(y+20,b_y+b_s)]
			if p1[0] < p2[0] and p1[1] < p2[1]:
				self.extend()
				self.score += 1
				TICK +=0.05
				bonus.remove(bonu)
				bonus.append(Bonus())
		return TICK

	


	def isOut (self):
		x = self.pos[0][0]
		y = self.pos[0][1]
		return x<0 or x>380 or y < 0 or y > 380

	def extend(self):
		self.pos.append((self.pos[-1][0] + self.key[0]*SPEED,self.pos[-1][1] + self.key[1]*SPEED))
		self.size+=1

class Bonus :

	def __init__(self):
		self.pos = (r(40,340),r(40,340))
		self.size = choice(sizeList)
		self.img = pygame.Surface(self.size)
		self.img.fill(choice(BONUS_COLOR))

	def show(self,surface):
		surface.blit(self.img,self.pos)

			
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
display = pygame.display.set_mode((400,400))
texte = dialogue_font = pygame.font.SysFont('arial', 15)
end = dialogue_font = pygame.font.SysFont('franklingothicmedium', 35)

snack = Snack()
continu = True
game = True
showEnd = 1
start = 5 
while start :
	display.fill((0,0,0))
	name = texte.render("Start :"+str(start), True, (145,24,255))
	display.blit(name,(160,220))
	pygame.display.update()
	start -= 1
	pause(1)

while continu : 
	clock.tick(2)
	for event in pygame.event.get():  
		if event.type == QUIT:    
			continu = False
			game = False
		if event.type == KEYDOWN:
			if event.key == K_SPACE:
				game = True
				snack = Snack()
				TICK = 7
				start = 5
				while start :
					display.fill((0,0,0))
					name = texte.render("Start :"+str(start), True, (145,24,255))
					display.blit(name,(160,220))
					pygame.display.update()
					start -= 1
					pause(1)
			if event.key == K_RETURN:
				continu = False
				game = False
	while game :
		clock.tick(int(TICK))
		for event in pygame.event.get():  
			if event.type == QUIT:    
					continu = False
					game = False
			if event.type == KEYDOWN:
				if event.key == K_LEFT or event.key == K_q :
					if snack.key != (1,0):
						snack.key = (-1,0)
				if event.key == K_RIGHT  or event.key == K_d:
					if snack.key != (-1,0):
						snack.key = (1,0)
				if event.key == K_UP  or event.key == K_z:
					if snack.key != (0,1):
						snack.key = (0,-1)
				if event.key == K_DOWN or event.key == K_s:
					if snack.key != (0,-1):
						snack.key = (0,1)
				# if event.key == K_a:
				# 	snack.extend()

		display.fill((0,0,0))

		snack.move()
		snack.show(display)
		if snack.isOut():
			game = False
		bonus_state+=1
		if bonus_state == BONUS_SPAWN():
			bonus_state = 0
			bonus.append(Bonus())
		TICK = snack.colide(bonus,TICK)
		for element in bonus:
			element.show(display)
		name = texte.render("score : "+str(snack.score)+" Speed : "+str(int(TICK)), True, (0,0,255))
		display.blit(name,(0,0))
		pygame.display.update()
	gameOver = end.render('Game over !', True, (255,0,25))
	replay = texte.render("Press space to restart or enter to quit", True, (255,255,255))
	display.fill((0,0,0))
	display.blit(gameOver,(130,180))
	name = texte.render("score : "+str(snack.score), True, (0,0,255))
	display.blit(name,(160,220))
	if showEnd == 1:
		display.blit(replay,(100,250))
	showEnd = -1*showEnd
	pygame.display.update()