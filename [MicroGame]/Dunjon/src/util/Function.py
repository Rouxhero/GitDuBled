import pygame
from pygame.locals import *

# VAR MOUVEMENT
LEFT =-1
RIGHT= 1
UP   =-1
DOWN = 1
NONE = 0

def PyImgLoad(path:str,size:tuple):
	return pygame.transform.scale(pygame.image.load(path),size)

def PyPrint(text,color,font):
	return font.render(text, False, color)


def PySquare(size:tuple,color=(0,0,0)):
	img = pygame.Surface(size)
	img.fill(color)
	return img


