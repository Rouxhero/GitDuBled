from util.Function import *
from util.Object import *
from util.Game import *	


game = Game((600,600))
pygame.key.set_repeat(10)
while game.play:
	for event in pygame.event.get():
		# Close if the user quits the game
		if event.type == QUIT:
			game.over()
		if event.type == KEYDOWN:
			if event.key == K_UP:
				game.player.move(NONE,UP)
			if event.key == K_DOWN:
				game.player.move(NONE,DOWN)
			if event.key == K_LEFT:
				game.player.move(LEFT)
			if event.key == K_RIGHT:
				game.player.move(RIGHT)

	game.show()
	pygame.display.update()