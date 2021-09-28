import tkinter as tk
import tkinter.ttk as tkk
from tkinter.filedialog import *
from interface.entry import *
from regex import *
from RegUtil.data import *
import re



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
		self.edite = None # package,class,var,func
		self.umlCode = {
			"package1":
				{
				"class1":
					{
					"var":['Player'],
					"func":['getPlayer']
					}
				}
			}#{pack:{class:{var:[],func:[]}}}
		self.status = tk.LabelFrame(
			self, text="Uml Resume", borderwidth=2, relief=GROOVE
		)
		self.statusTExt = StringVar()

		self.pos = {"option": 0,}
		self.__setOption()
		self.__setStatus()


	def __setOption(self):
		for key in self.optionDicts:
			self.Button[key] = tk.Button(
				self.optionAsk,
				text=key,
				command=self.optionDicts[key],
				).grid(column=self.pos["option"], row=0, sticky="nsew",padx="30",pady="15")
			self.pos["option"] += 1
			self.optionAsk.grid(column=0, row=0,columnspan=3)


	def __setStatus(self):
		scrollbar = tk.Scrollbar(self.status)
		scrollbar.grid(column=1,row=0)
		self.output_label =tk.Listbox(self.status,yscrollcommand=scrollbar.set,width=20,height=20,) 
	
		self.output_label.grid(column=0,row=0,sticky="w")
		self.status.grid(column=0, row=1)

	def __setPackage(self):     
		self.output_label.delete(0,tk.END)
		for pack in self.umlCode:
			self.output_label.insert(tk.END,pack)
			for clas in self.umlCode[pack]:
				self.output_label.insert(tk.END,space*4+"L"+clas)
				for var in self.umlCode[pack][clas]['var']:
					self.output_label.insert(tk.END,space*8+" L"+var)
				for func in self.umlCode[pack][clas]['func']:
					self.output_label.insert(tk.END,space*8+" L"+func)
				self.output_label.insert(tk.END,"")
			self.output_label.insert(tk.END,"")
		# self.statusTExt.set(text)
	def __setClass(self):
		pass
	def __setVar(self):
		pass
	def __setFunc(self):
		pass


