import tkinter as tk
import tkinter.ttk as tkk
from tkinter.filedialog import *
from interface.entry import *
from regex import *
from RegUtil.data import *
import re


state = {
	"None":{"Package":"normal","Class":"normal","Var":"disabled","Func":"disabled"},
	"Package":{"Package":"disabled","Class":"normal","Var":"disabled","Func":"disabled"},
	"Class":{"Package":"disabled","Class":"disabled","Var":"normal","Func":"normal"},
	"Var":{"Package":"disabled","Class":"disabled","Var":"normal","Func":"normal"},
	"Func":{"Package":"disabled","Class":"disabled","Var":"normal","Func":"normal"}, 
}

PackageOpt = {
	"Name":"entry",
}
ClassOpt = {
	"Name":"entry",
	"abstract":"Check",
	"Protected":"Check",
}

returnOPt = {
	"abstract":{0:"",1:"abstract"},
	"Protected":{0:"",1:"abstract"},
	
}

class UmlPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.columnconfigure(1, weight=1)
		self.columnconfigure(2, weight=1)
		# Flieds for UML Add
		self.optionDicts = {
			"Package":self.__setPackage,
			"Class":self.__setClass,
			"Var":self.__setVar,
			"Func":self.__setFunc,
		}
		self.Button = {}
		self.optionAsk = tk.LabelFrame(
			self, text="Add Something", borderwidth=2, relief=GROOVE
		)

		# Fields for UML Status
		self.edite = "None" # package,class,var,func
		self.cursor = "None"
		self.varSave = {"Package":[],"Class":[],"Var":[],"Func":[]}
		self.umlCode = {}
			# "package1":
			# 	{
			# 	"class1":
			# 		{
			# 		"stat":True,
			# 		"var":['# Int Player'],
			# 		"func":['+ getPlayer():Player']
			# 		}
			# 	}
			# }#{pack:{class:{var:[],func:[]}}}
		self.status = tk.LabelFrame(
			self, text="Uml Resume", borderwidth=2, relief=GROOVE
		)
		self.pos = {"option": 0,}


		# Fields For all Editor
		self.__setOption()
		self.__setStatus()


	def __setOption(self):
		for key in self.optionDicts:
			self.Button[key] = tk.Button(
				self.optionAsk,
				text=key,
				command=self.optionDicts[key],
				state=state[self.edite][key],
				)
			self.Button[key].grid(column=self.pos["option"], row=0, sticky="nsew",padx="30",pady="15")
			self.pos["option"] += 1
			self.optionAsk.grid(column=0, row=0,columnspan=3)


	def __setStatus(self):
		scrollbar = tk.Scrollbar(self.status)
		scrollbar.grid(column=1,row=0)
		self.output_label =tk.Listbox(self.status,yscrollcommand=scrollbar.set,width=20,height=20,) 
	
		self.output_label.grid(column=0,row=0,sticky="w")
		self.status.grid(column=0, row=1)

	def __setPackage(self):  
		self.Editor = tk.LabelFrame(
			self, text="Editor", borderwidth=2, relief=GROOVE
		)
		index = 0
		self.edite = "Package"
		self.cursor = "Package"
		self.__updateButton()
		for option in PackageOpt:
				tk.Label(self.Editor,text=option).grid(column=0,row=index)
				if PackageOpt[option] == "entry":
					self.varSave['Package'].append(tk.Entry(self.Editor,width=20, justify="center"))
					# self.varSave[-1].bind("<Key>", self.__ValideEdite)
					self.varSave['Package'][-1].grid(column=3, row=index)
				index+=1
		tk.Button(self.Editor,text="Valide",command=self.__ValideEdite).grid(column=1,row=index)
		self.Editor.grid(column=1, row=1)
	def __setClass(self):
		self.Editor = tk.LabelFrame(
			self, text="Editor", borderwidth=2, relief=GROOVE
		)
		index = 0
		self.edite = "Class"
		self.__updateButton()
		for option in ClassOpt:
				if ClassOpt[option] == "entry":
					tk.Label(self.Editor,text=option).grid(column=0,row=index)
					self.varSave['Class'].append(tk.Entry(self.Editor,width=20, justify="center"))
					# self.varSave[-1].bind("<Key>", self.__ValideEdite)
					self.varSave['Class'][-1].grid(column=3, row=index)
				elif ClassOpt[option] == "Check":
					self.varSave['Class'].append(IntVar())
					tk.Checkbutton(
                    self.Editor,
                    text=option,
                    variable=self.varSave['Class'][-1],
                    onvalue=1,
                    offvalue=0,
                ).grid(row=index, column=0, sticky="w")
				index+=1
		tk.Button(self.Editor,text="Valide",command=self.__ValideEdite).grid(column=1,row=index)
		self.Editor.grid(column=1, row=1)
	def __setVar(self):
		pass
	def __setFunc(self):
		pass

	def __updateButton(self):
		for key in self.Button:
			self.Button[key].config(state=state[self.edite][key],)
	def __ValideEdite(self):
		data = self.varSave[self.edite]
		if self.edite == "Package":
			self.umlCode[data[0].get()]={}
		elif self.edite == "Class":
			newData = []
			for dat in data[1:]:
				newData.append(dat.get())
			if self.cursor != "None":
				self.umlCode[self.cursor][data[0].get()] = newData
			else :
				self.umlCode[data[0].get()] = newData

		self.edite = self.cursor
		self.__updateButton()
		self.output_label.delete(0,tk.END)
		for pack in self.umlCode:
			self.output_label.insert(tk.END,pack)
			for clas in self.umlCode[pack]:
				self.output_label.insert(tk.END,space*4+"L"+clas)
				if self.umlCode[pack][clas]['stat']:
					for var in self.umlCode[pack][clas]['var']:
						self.output_label.insert(tk.END,space*8+" L"+var)
					for func in self.umlCode[pack][clas]['func']:
						self.output_label.insert(tk.END,space*8+" L"+func)
					self.output_label.insert(tk.END,"")
			self.output_label.insert(tk.END,"")
		# self.statusTExt.set(text)