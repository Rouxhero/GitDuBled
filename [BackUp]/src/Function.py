import os


if os.name == "posix":
	clear = lambda : os.system('clear')
	separator = '/'
else:
	clear = lambda : os.system('cls')
	separator = '\\'


    
 
   