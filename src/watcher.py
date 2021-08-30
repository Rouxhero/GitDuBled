import threading
from Function import *
import re

class Watcher(threading.Thread) :


	def __init__(self,path):
		# variable set :

		#  path of watcher
		self.path = path
		#  liste of all files watched
		self.data = []
		self.dirs = []
		# dict with all backup linked with the floder
		self.backUp = {"1":path+"/.backup/B1"}
		self.Actualbackup = 1
		# List of all ignored floder
		self.ignore = ['.git','__pycache__','.backup']
		# cache for all files of self.data
		self.cached_stamp_floder = {}
		self.cached_stamp_file = {}
		# Creating backup floder
		os.system("mkdir {}.backup".format(path+separator))
		# first backup + reading data
		for path, dirs, files in os.walk(self.path):
			if all(not ignore in path.split(separator) for ignore in self.ignore):
				for floder in dirs:
					if not floder in self.ignore:
						self.dirs.append(path+separator+floder)
						self.cached_stamp_floder[path+separator+floder] = {"stamp":os.stat(path+separator+floder).st_size}
				for file in files:
					end = file.split('.')
					if len(end) > 1 :
						end = end[-1]
						self.data.append(path+separator+file)
						self.cached_stamp_file[path+separator+file] = {"stamp":os.stat(path+separator+file).st_mtime, "type":end, "backUp":"1"}
		self.save()
		self.save()
		self.save()
		self.save()
		self.save()

	def save(self):
		for dirs in  self.dirs:
			dirs =  dirs[len(self.path):]
			os.system("mkdir {}.backup{}{}".format(self.path+separator,separator+"B"+str(self.Actualbackup),separator+dirs))
		

		self.Actualbackup +=1
		self.backUp[str(self.Actualbackup)] = self.path+"/.backup/B"+str(self.Actualbackup)

if __name__ == '__main__':
	test = Watcher('E:\\Desktop\\Programmation\\gitDuBled')
	print(test.dirs)
	print(test.cached_stamp_floder)