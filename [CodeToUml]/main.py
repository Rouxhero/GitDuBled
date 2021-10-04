from run.interface import *
import urllib.request

statu = True
try :
	urllib.request.urlopen('https://www.google.fr')
except Exception as e:
	statu = False
	print("OffLine Launch")

if statu :
	updateV = urllib.request.urlopen('https://www.github.com/Rouxhero/GitDuBled/')s

