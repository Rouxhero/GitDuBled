from util.Function import *
from util.Object import *
from util.Game import *


game = Game((400,400))
for y in range(10):
	game.object.append(Wall((0,y*40),(40,40)))
	game.object.append(Wall((360,y*40),(40,40)))
	game.object.append(Wall((y*40,360),(40,40)))
	game.object.append(Wall((y*40,0),(40,40)))

while game.play:
	for event in pygame.event.get():

		# Close if the user quits the game
		if event.type == QUIT:
			game.over()

	game.show()
	pygame.display.update()