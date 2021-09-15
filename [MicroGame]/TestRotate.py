# Python program to transform the
# image with the mouse

#Import the libraries pygame and math
import pygame
import math
from pygame.locals import *
import os

# Take colors input
RED = (255, 0, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

#Construct the GUI game
pygame.init()

#Set dimensions of game GUI
w, h = 600, 440
screen = pygame.display.set_mode((w, h))

# Set running, angle and scale values
running = True
angle = 0
scale = 1

# Take image as input
img_logo = pygame.image.load('player.png')
img_logo.convert()

# Draw a rectangle around the image
rect_logo = img_logo.get_rect()
pygame.draw.rect(img_logo, RED, rect_logo, 1)

# Set the center and mouse position
center = w//2, h//2
mouse = pygame.mouse.get_pos()

#Store the image in a new variable
#Construct the rectangle around image
img = img_logo
rect = img.get_rect()
rect.center = center
os.system('python3 snack.py &')
# Setting what happens when game is
# in running state
while running:
	for event in pygame.event.get():

		# Close if the user quits the game
		if event.type == QUIT:
			running = False

		# Set at which angle the image will
		# move left or right
		if event.type == KEYDOWN:
			if event.key == K_a:
				if event.mod & KMOD_SHIFT:
					angle -= 5
				else:
					angle += 5

			# Set at what ratio the image will
			# decrease or increase
			elif event.key == K_a:
				if event.mod & KMOD_SHIFT:
					scale /= 1.5
				else:
					scale *= 1.5
				
		# Move the image with the specified coordinates,
		# angle and scale		
		elif event.type == MOUSEMOTION:
			mouse = event.pos
			x = mouse[0] - center[0]
			y = mouse[1] - center[1]
			d = math.sqrt(x ** 2 + y ** 2)
			angle = math.degrees(-math.atan2(y, x))
			# scale = abs(5 * d / w)
			img = pygame.transform.rotate(img_logo, angle)
			rect = img.get_rect()
			rect.center = center
	
	# Set screen color and image on screen
	screen.fill(YELLOW)
	screen.blit(img, rect)

	# Draw the rectangle, line and circle through
	# which image can be transformed
	pygame.draw.rect(screen, BLACK, rect, 3)
	pygame.draw.line(screen, RED, center, mouse, 2)
	pygame.draw.circle(screen, RED, center, 6, 1)
	pygame.draw.circle(screen, BLACK, mouse, 6, 2)
	
	# Update the GUI game
	pygame.display.update()

# Quit the GUI game
pygame.quit()
