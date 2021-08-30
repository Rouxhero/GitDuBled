import threading
from Function import *


class Watcher(threading.Thread) :


	def __init__(self,path):
		# variable set :

		#  path of watcher
		self.path = path
		#  liste of all files watched
		self.data = []
		# dict with all backup linked with the floder
		self.backUp = {"01":path+"/.backup/B01"}
		# List of all ignored floder
		self.ignore = ['.git','__pycache__','.backup']
		# cache for all files of self.data
		self.cached_stamp = {}
		# Creating backup floder
		os.system("mkdir {}.backup".format(path+separator))
		# first backup + reading data
		for path, dirs, files in os.walk(self.path):
			if all(not ignore in path.split(separator) for ignore in self.ignore):
				for file in files:
					end = file.split('.')
					if len(end) > 1 :
						end = end[-1]
						self.data.append(path+separator+file)
						self.cached_stamp[path+separator+file] = {"stamp":os.stat(path+separator+file).st_mtime, "type":end, "backUp":"01"}



if __name__ == '__main__':
	test = Watcher('E:\\Desktop\\Programmation\\gitDuBled')
	print(test.data)
	print(test.cached_stamp)