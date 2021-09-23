 #!/usr/bin/env python3
 


def checkPos(maps,typeTile,x,y):
	# print("test for {} at {},{}".format(typeTile,x,y))
	state = type(maps[x][y]) == Ground
	stateV = False
	if x+1 < len(maps):
		stateV = stateV or type(maps[x+1][y]) == typeTile
	if x > 1 :
		stateV = stateV or  type(maps[x-1][y]) == typeTile
	if y+1 < len(maps[0]):
		stateV = stateV or  type(maps[x][y+1]) == typeTile
	if y > 1 :
		stateV = stateV or  type(maps[x][y-1]) == typeTile
	return state and stateV and True