#!/usr/bin/env python3
import pygame
from pygame.locals import *


def PyImgLoad(path:str,size:tuple):
	return pygame.transform.scale(pygame.image.load(path),size)

def PyPrint(text,color,font):
	return font.render(text, False, color)

def maps(lists,func):
	newList = []
	for el in lists:
		newList.append(func(el))
	return newList
