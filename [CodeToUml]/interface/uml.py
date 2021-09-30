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
headR = {
	"|":"Package",
	"@":"Class"
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

		# Fields of path
		self.pathList = []
		self.indexPath = 0
		self.pathUml = tk.LabelFrame(
			self,text="Path :", borderwidth=2, relief=GROOVE,
		)
		self.pathUmlTxt = StringVar()
		self.pathUmlTxt.set("/")
		tk.Label(self.pathUml,textvariable=self.pathUmlTxt, width=50,
                bg="white",
                borderwidth=2,
                relief=GROOVE,).grid(column=0,row=0,sticky="w")
		self.pathUml.grid(column=0,row=1,columnspan=3)
		self.moveButton = {}
		self.moveButton["Left"] = tk.Button(
				self.pathUml,
				text="<",
				command=self.__moveLeft,
				state="disabled",
				)
		self.moveButton["right"] = tk.Button(
				self.pathUml,
				text=">",
				command=self.__moveRight,
				state="disabled",
				)
		self.moveButton["Left"].grid(column=1,row=0,sticky="w")
		self.moveButton["right"].grid(column=2,row=0,sticky="w")
		self.__updateButton()


	def __moveLeft(self):
		self.indexPath -= 1
		self.cursor = self.pathList[self.indexPath]
		self.edite = headR[self.pathList[self.indexPath][0]]
		print("<"+self.cursor,self.edite)
		self.__updateButton()
		self.__updateSate()
	def __moveRight(self):
		self.indexPath += 1
		self.cursor = self.pathList[self.indexPath]
		self.edite = headR[self.pathList[self.indexPath][0]]
		print(">"+self.cursor,self.edite)
		self.__updateButton()
		self.__updateSate()

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
		self.status.grid(column=0, row=2)

	def __setPackage(self):  
		self.Editor = tk.LabelFrame(
			self, text="Editor", borderwidth=2, relief=GROOVE
		)
		index = 0
		self.edite = "Package"
		self.cursor = "None"
		self.__updateButton()
		for option in PackageOpt:
				tk.Label(self.Editor,text=option).grid(column=0,row=index)
				if PackageOpt[option] == "entry":
					self.varSave['Package'].append(tk.Entry(self.Editor,width=20, justify="center"))
					# self.varSave[-1].bind("<Key>", self.__ValideEdite)
					self.varSave['Package'][-1].grid(column=3, row=index)
				index+=1
		tk.Button(self.Editor,text="Valide",command=self.__ValidePack).grid(column=1,row=index)
		self.Editor.grid(column=1, row=2)


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
		tk.Button(self.Editor,text="Valide",command=self.__ValideClass).grid(column=1,row=index)
		self.Editor.grid(column=1, row=2)


	def __setVar(self):
		pass
	def __setFunc(self):
		pass

	def __updateButton(self):
		print(self.pathList)
		for key in self.Button:
			self.Button[key].config(state=state[self.edite][key])
		if self.indexPath <= 0 :
			self.moveButton["Left"].config(state="disabled")
			self.moveButton["right"].config(state="disabled")
		elif self.indexPath > 0:
			self.moveButton["Left"].config(state="normal")
		elif self.indexPath > len(self.pathList) :
			self.moveButton["right"].config(state="disabled")
		elif self.indexPath <= len(self.pathList):
			self.moveButton["right"].config(state="normal")
			

	def __ValidePack(self):
		data = self.varSave[self.edite]
		name = "|"+data[0].get()
		self.umlCode[name]={}
		self.cursor =name
		self.edite = "Package"
		self.Editor.destroy()
		self.pathList.append(name)
		self.indexPath += 1
		self.pathUmlTxt.set("/"+name[1:]+"/")
		self.__updateButton()
		self.__updateSate()

	def __ValideClass(self):
		data = self.varSave[self.edite]
		name = "@"+data[0].get()
		if self.cursor.split(';')[-1] != "None":
			self.umlCode[self.cursor][name]={"stat":True,"var":[],"func":[]}
		else :
			self.umlCode[name]={"stat":True,"var":[],"func":[]}
		self.cursor = name
		self.edite = "Class"
		self.Editor.destroy()
		self.pathList.append(name)
		self.indexPath += 1
		old = str(self.pathUmlTxt.get())
		self.pathUmlTxt.set(old+name[1:]+"/")
		self.__updateButton()
		self.__updateSate()

		

	def __updateSate(self):
		self.output_label.delete(0,tk.END)
		for key in self.umlCode:
			if key[0] == '|':
				pack = key[1:]
				self.output_label.insert(tk.END,pack)
				for clas in self.umlCode[key]:
					clasN = clas[1:]
					self.output_label.insert(tk.END,space*4+"L"+clasN)
					if self.umlCode[key][clas]['stat']:
						for var in self.umlCode[key][clas]['var']:
							self.output_label.insert(tk.END,space*8+" L"+var)
						for func in self.umlCode[key][clas]['func']:
							self.output_label.insert(tk.END,space*8+" L"+func)
						self.output_label.insert(tk.END,"")
			else :
				clasN = key[1:]
				self.output_label.insert(tk.END,space*4+"L"+clasN)
				if self.umlCode[key]['stat']:
					for var in self.umlCode[key]['var']:
						self.output_label.insert(tk.END,space*8+" L"+var)
					for func in self.umlCode[key]['func']:
						self.output_label.insert(tk.END,space*8+" L"+func)
					self.output_label.insert(tk.END,"")
			self.output_label.insert(tk.END,"")

		# Etape :=> check in/out pack => Validate Class, check int/out class => validate var/func
		# use validate Pack,validate Class, validate components !
