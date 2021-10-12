import tkinter as tk
import tkinter.ttk as tkk
from tkinter.filedialog import *
from interface.entry import *
from regex import *
from interface.uml import *
from interface.function import *
import re


class CodePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.MultiFileflag = {
            "ProjectPath":"",
            "showPackage":None,
            "showRelation":None,
        }
        self.OneFileflag = {
            "File  Path":"",
            "showPackage":None,
            "showRelation":None,
        }