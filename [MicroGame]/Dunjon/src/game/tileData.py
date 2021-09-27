tileData = {}
boolConv = {"true":True,"false":False}
with open("tile.data","r") as file :
	line = file.readline()
	while line :
		if line[0] != "#":
			data = line.split(';')
			if len(data) == 6 :
				tileData[int(data[1])] = {
				"pack":data[0],
				"file":data[3],
				"name":data[2],
				"break":boolConv[data[4]]
				}
		line = file.readline()

print(tileData)