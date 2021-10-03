##!/usr/bin/env python3
from RegUtil.data import *


class Import :

	def __init__(self,packList):
		self.data = packList
		self.__genImport()



	def __genImport(self):
		allClassName = {}
		for pack in self.data:
			for clas in pack.classData:
				allClassName[(clas.flag['name'])] = [clas.types,clas,pack.name]
		print(allClassName.keys())
		txt = ""
		for tpe in allClassName:
			tpEE = allClassName[tpe]
			txt = ""
			for tps in tpEE[0]:
				tps = cleanTT(tps)
				print(tps)
				tps = tps.split('<')
				print(tps)
				tpss = tps
				tps = []
				for tt in tpss:
					allD = tt.split(',')
					for al in allD:
						tps.append(al)
				print(tps)
				for tt in tps :
					print(tt)
					tt = tt.split('>')[0]
					if tt in importVal :
						txt += importVal[tt]+line
					elif not tt in NoImport:
						if tt in allClassName :
							target = allClassName[tt][2]
							txt += "import {}.{} ;".format(target,tt)+line
			tpEE[1].imports = txt

 
