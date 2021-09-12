import tkinter as tk
import tkinter.ttk as tkk
from tkinter.filedialog import *
from interface.entry import *
from regex import *


def selecPath():
    return askdirectory()


def selectFile():
    return askopenfilename(
        title="Open WSD file", filetypes=[("wsd files", ".wsd"), ("all files", ".*")]
    )


defauldName = {
    "path": "path/to/project",
    "Floder Name": "Name of the floder project",
    "Project Name": "Name of project",
    "wsd file": "path/to/file.wsd",
}


class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        # Variable Config :
        self.var = {
            "path": None,
            "Project Name": None,
            "Floder Name": None,
            "wsd file": None,
        }
        self.func = defauldName = {
            "path": self.changePath,
            "Project Name": self.changeName,
            "Floder Name": self.changeFloder,
            "wsd file": self.changeWsd,
        }
        self.entree = {}
        self.entreeState = {}
        self.varAsk = tk.LabelFrame(
            self, text="Configure Import", borderwidth=2, relief=GROOVE
        )

        # Option Config :
        self.option = {
            "code": tk.IntVar(),
            "test": tk.IntVar(),
            "MakeFile": tk.IntVar(),
            "Readme": tk.IntVar(),
        }
        self.fields = {}
        self.MakeFileOption = tk.IntVar()
        self.jar = {"main": tk.StringVar(),}
        self.optionAsk = tk.LabelFrame(
            self, text="Setting", borderwidth=2, relief=GROOVE
        )

        # Status Config :
        self.status = {"status": tk.StringVar(),"msg":tk.StringVar()}
        self.status["status"].set("Pending")
        self.output = tk.LabelFrame(self, text="Process", borderwidth=2, relief=GROOVE)
        
        # JAR CONFIG 😁

        self.MakeFileConfig = tk.LabelFrame(self, text="makeFile config", borderwidth=2, relief=GROOVE)


        # Position
        self.pos = {"var":0,"option":0,"status":0}


        # Show all part
        self.__setHead()
        self.__setEntry()
        self.__setOption()
        self.__showStatu()


        # Final Button :
        tk.Button(
            self,
            text="GOOOOOOOOO",
            command=self.work,
            relief=GROOVE,
            borderwidth=2,
            activebackground="green",
        ).grid(row=4, column=1, columnspan=3, sticky="nsew")    

    def __setHead(self):
        # Title
        tk.Label(self, text="Welcom to UML to Code !").grid(
            row=0, column=1, sticky="nsew", columnspan=3
        )
        # For WoaW
        tk.Label(self, text="").grid(row=0, column=1, sticky="nsew")
        tk.Label(self, text="").grid(row=1, column=0, sticky="nsew")
        tk.Label(self, text="").grid(row=0, column=4, sticky="nsew")
        tk.Label(self, text="").grid(row=3, column=0, sticky="nsew")
        tk.Label(self, text="").grid(row=5, column=0, sticky="nsew")


    def __setEntry(self):
        for key in defauldName:
            # Variable Text
            self.var[key] = tk.StringVar()
            self.var[key].set(defauldName[key])

            # Show First Text 
            tk.Label(self.varAsk, text="{} :".format(key)).grid(
                row=self.pos['var'], column=0, sticky="nsew"
            )
            if key != "Project Name" and key != "Floder Name":
                self.output_label = tk.Label(
                    self.varAsk,
                    textvariable=self.var[key],
                    width=50,
                    bg="white",
                    borderwidth=2,
                    relief=GROOVE,
                )
                self.output_label.grid(column=1, row=self.pos['var'])
                tk.Button(self.varAsk, text="...", command=self.func[key]).grid(
                    row=self.pos['var'], column=2, sticky="e"
                )
            else:
                self.entree[key] = [tk.Entry(self.varAsk, width=50, justify="center"),tk.IntVar()]
                self.entree[key][0].bind('<Return>', self.func[key])
                self.entree[key][0].grid(column=1, row=self.pos['var'])
                self.entreeState[key] = tk.Checkbutton(
                    self.varAsk,
                    variable=self.entree[key][1],
                    onvalue=1,
                    offvalue=0,
                    state="disabled"
                ).grid(row=self.pos['var'], column=3, sticky="e")
            tk.Label(self.varAsk, text="").grid(
                row=self.pos['var'] + 1, column=0, sticky="nsew"
            )

            self.pos['var'] += 2
        tk.Label(self.varAsk, text="").grid(row=0, column=4, sticky="w")
        self.varAsk.grid(column=1, row=1, columnspan=3)

    def __setOption(self):
        for key in self.option:
            if key == "MakeFile":
                tk.Checkbutton(
                    self.optionAsk,
                    text=key,
                    variable=self.option[key],
                    onvalue=1,
                    offvalue=0,
                    command=self.MakeFile,
                ).grid(row=self.pos['option'], column=0, sticky="w")
            else:
                tk.Checkbutton(
                    self.optionAsk,
                    text=key,
                    variable=self.option[key],
                    onvalue=1,
                    offvalue=0,
                ).grid(row=self.pos['option'], column=0, sticky="w")
            self.pos['option'] += 1
        tk.Label(self.optionAsk, text="").grid(row=0, column=4, sticky="e")
        self.optionAsk.grid(column=1, row=2)

    def __showStatu(self):

        for key in self.status:
            tk.Label(self.output, text="{} :".format(key)).grid(
                row=self.pos['status'], column=0, sticky="nsew"
            )
            self.output_label = tk.Label(
                self.output,
                textvariable=self.status[key],
                width=10,
                bg="white",
                borderwidth=2,
                relief=GROOVE,
            ).grid(row=self.pos['status'], column=1, sticky="nsew")
            self.pos['status'] += 1
        tk.Label(self.output, text="").grid(row=0, column=4, sticky="e")
        self.output.grid(column=3, row=2)

    def changePath(self):
        self.var["path"].set(selecPath())

    def changeWsd(self):
        self.var["wsd file"].set(selectFile())

    def changeName(self,key):
        text = self.entree["Project Name"][0].get()
        if text != "":
            self.entree["Project Name"][1].set(1)
            self.var["Project Name"].set(text)
    def changeJar(self,key):
        text = self.entree["jar"][0].get()
        if text != "":
            self.entree["jar"][1].set(1)
            self.jar['main'].set(text)
    def changeFloder(self,key):
        text = self.entree["Floder Name"][0].get()
        if text != "":
            self.entree["Floder Name"][1].set(1)
            self.var["Floder Name"].set(text)

    def MakeFile(self):
        tk.Checkbutton(
            self.MakeFileConfig,
            text="Add jar Build ",
            variable=self.MakeFile,
            onvalue=1,
            offvalue=0,
            command=self.configJar,
        ).grid(row=0, column=0, sticky="w")
        self.MakeFileConfig.grid(column=2, row=2)


    def configJar(self):
        tk.Label(self.MakeFileConfig, text="Main :").grid(
                row=1, column=0, sticky="nsew"
            )
        self.entree["jar"] = [tk.Entry(self.MakeFileConfig, width=20, justify="center"),tk.IntVar()]
        self.entree["jar"][0].bind('<Return>', self.changeJar)
        self.entree["jar"][0].grid(column=1, row=1)
        self.entreeState["jar"] = tk.Checkbutton(
            self.MakeFileConfig,
            variable=self.entree["jar"][1],
            onvalue=1,
            offvalue=0,
            state="disabled"
        ).grid(row=1, column=3, sticky="e")

    def work(self):
        etat = True
        for key in self.var:
            if self.var[key].get() == defauldName[key]:
                etat = False
                self.status["msg"].set("ImportError")
        if etat:
            arg = {}
            arg['path'] = path = self.var["path"].get()
            arg["fatherRep"] = self.var["Floder Name"].get()
            arg["projectName"] = self.var["Project Name"].get()
            arg["wsdPath"] = self.var["wsd file"].get()
            arg["output"] =   self.status["status"]
            self.status["status"].set("Running")
            try:
                runRegex(arg)
            except Exception as e:
                print(e)
                self.status["msg"].set(e)
                etat = False
        if etat:
            self.status["status"].set("Succes")
            self.status["msg"].set("")
        else:
            self.status["status"].set("Error")


FramesList = (MainPage,)