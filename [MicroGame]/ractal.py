import turtle as t
from time import sleep as pause
t.speed(-1)
def ptsNtm(x,y):
	xA = x[0]
	yA = x[1]
	xB = y[0]
	yB = y[1]
	return ((xA+xB)//2+(yB-yA)//2,(yA+yB)//2+(xA-xB)//2)

def pasDrag(path):
	if len(path) >=2:
		return [path[0],ptsNtm(path[0],path[1]),path[1]]+pasDrag(path[1:])
	else :
		return path

def cleanList(liste):
	stock = []
	for x in liste :
		if not x in stock :
			stock.append(x)
	return stock
t.hideturtle()
x = (0, 0)
y = (0, 200)
path = [x,y]
path = cleanList(pasDrag([x,y]))
for x in range(1):
	path = pasDrag(path)
print(path)
for coord in path :
	t.goto(coord)
pause(1)
# t.setpos(0,0)
# t.clear()