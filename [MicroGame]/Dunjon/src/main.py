from util.Function import *
from util.Object import *
from util.Game import *


game = Game((900,600))

while game.play:
	for event in pygame.event.get():

		# Close if the user quits the game
		if event.type == QUIT:
			game.over()

	game.show()
	pygame.display.update()