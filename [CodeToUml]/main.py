from run.interface import *
import urllib.request

statu = True
try :
	urllib.request.urlopen('https://www.google.fr')
except Exception as e:
	statu = False
	print("OffLine Launch")



def update():
	allFIle = open("data/file","r").read().split('\n')
	for file in allFIle:
		if file[0] != "#":
			url = "https://raw.githubusercontent.com/Rouxhero/GitDuBled/master/%5BCodeToUml%5D/{}".format(file)
			print('Downloading : ',url,end=":")
			data = urllib.request.urlopen(url).read().decode()
			open(file,'w').write(data)
			print("Done")
	print("\nUpdate Done")
print("Check Update : ",end="")
# if statu :
# 	updateV = urllib.request.urlopen('https://raw.githubusercontent.com/Rouxhero/GitDuBled/master/%5BCodeToUml%5D/data/version').read().decode()
# 	version = open('data/version','r').read()
# 	if version!=updateV:
# 		print("Needs Update")
# 		update()
# 	else:
# 		print("OK")

update()

