import tkinter as tk
import tkinter.ttk as tkk
from tkinter.filedialog import *
from interface.entry import *
from regex import *


def selecPath():
    return askdirectory() 
def selectFile():
    return askopenfilename(title="Open WSD file",filetypes=[('wsd files','.wsd'),('all files','.*')])

defauldName = {"path":"path/to/project","Floder Name":"Name of the floder project","Project Name":"Name of project","wsd file":"path/to/file.wsd"}




class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowX = 0
        self.var = {"path":None,"Project Name":None,"Floder Name":None,"wsd file":None}
        self.entree = {}
        self.option = {"code":tk.IntVar()  ,"test":tk.IntVar()  ,"MakeFile":tk.IntVar()  ,"Readme":tk.IntVar()  }
        self.status = {"status":tk.StringVar()}
        self.status["status"].set("Pending")
        self.func = defauldName = {"path":self.changePath,"Project Name":self.changeName,"Floder Name":self.changeFloder,"wsd file":self.changeWsd}
        tk.Label(self, text="").grid(row=0, column=1, sticky="nsew")
        tk.Label(self, text="Welcom to UML to Code !").grid(row=0, column=1, sticky="nsew",columnspan=3)
        tk.Label(self, text="").grid(row=1, column=0, sticky="nsew")
        tk.Label(self, text="").grid(row=0, column=4, sticky="nsew")
        
        self.__setEntry()
        self.__setOption()
        self.__showStatu()
        tk.Label(self, text="").grid(row=3, column=0, sticky="nsew")
        tk.Label(self, text="").grid(row=5, column=0, sticky="nsew")
        tk.Button(self,text="GOOOOOOOOO",command=self.work, relief=GROOVE,borderwidth=2,activebackground="green").grid(row=4, column=1,columnspan=2, sticky="nsew")
        # # We use the switch_window_button in order to call the show_frame() method as a lambda function
        # switch_window_button = tk.Button(
        #     self,
        #     text="Go to the Side Page",
        #     command=lambda: controller.show_frame(SidePage),
        # )
        # switch_window_button.pack(side="bottom", fill=tk.X)
        
    def __setEntry(self):
        self.varAsk = tk.LabelFrame(self,text = "Configure Import", borderwidth=2, relief=GROOVE)
        for key in defauldName:
            self.var[key] = tk.StringVar() 
            self.var[key].set(defauldName[key])            
            tk.Label( self.varAsk, text="{} :".format(key)).grid(row=self.rowX, column=0, sticky="nsew")
            if key != "Project Name" and  key != "Floder Name":
                self.output_label = tk.Label( self.varAsk,textvariable= self.var[key],width=50,bg="white", borderwidth=2, relief=GROOVE)
                self.output_label.grid(column=1, row=self.rowX)
                tk.Button( self.varAsk,text="...",command=self.func[key]).grid(row=self.rowX, column=2, sticky="e")
            else :
                self.entree[key] = tk.Entry( self.varAsk,width=50,justify="center")
                self.entree[key].grid(column=1, row=self.rowX)
                tk.Button( self.varAsk,text="Done",command=self.func[key]).grid(row=self.rowX, column=2, sticky="e")
       
            tk.Label( self.varAsk, text="").grid(row=self.rowX+1, column=0, sticky="nsew")
            
            self.rowX += 2
        tk.Label(self.varAsk, text="").grid(row=0, column=4, sticky="w")
        self.varAsk.grid(column=1, row=1,columnspan=2)

    def __setOption(self):
        self.rowX =0
        self.optionAsk = tk.LabelFrame(self,text = "Setting", borderwidth=2, relief=GROOVE)
        for key in self.option :
            tk.Checkbutton(self.optionAsk, text = key, variable = self.option[key], onvalue = 1, offvalue = 0,).grid(row=self.rowX,column=0,sticky="w") 
            self.rowX += 1
        tk.Label(self.optionAsk, text="").grid(row=0, column=4, sticky="e")
        self.optionAsk.grid(column=1, row=2)

    def __showStatu(self):
        self.output = tk.LabelFrame(self,text = "Process", borderwidth=2, relief=GROOVE)
        for key in self.status :
            tk.Label( self.output, text="{} :".format(key)).grid(row=self.rowX, column=0, sticky="nsew")
            self.output_label = tk.Label( self.output,textvariable= self.status[key],width=10,bg="white", borderwidth=2, relief=GROOVE).grid(row=self.rowX,column=1,sticky="nsew") 
            self.rowX += 1
        tk.Label(self.output, text="").grid(row=0, column=4, sticky="e")
        self.output.grid(column=2, row=2)

    def changePath(self):
        self.var["path"].set(selecPath()) 
    def changeWsd(self):
        self.var["wsd file"].set(selectFile())
    def changeName(self):
        self.var["Project Name"].set(self.entree['Project Name'].get())
    def changeFloder(self):
        self.var["Floder Name"].set(self.entree['Floder Name'].get())

    def work(self):
        etat = True
        for key in self.var:
            if self.var[key].get() == defauldName[key] :
                etat = False    
        if etat :
            path = self.var["path"].get()
            fatherRep = self.var["Floder Name"].get()
            projectName = self.var["Project Name"].get()
            wsdPath = self.var["wsd file"].get()
            self.status["status"].set("Running")
            
            try :
                runRegex(path,fatherRep,projectName,wsdPath)
            except Exception as e:
                print(e)
                etat = False
        if etat :
            self.status["status"].set("Succes")
        else :
            self.status["status"].set("Error")
FramesList = (MainPage,)