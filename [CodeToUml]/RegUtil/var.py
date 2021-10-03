##!/usr/bin/env python3
# classF file for Variable Object
from RegUtil.data import *


class Variable:
    def __init__(self, data):
        self.data = data
        self.flag = {"security": "", "static": "", "final": "", "text": ""}
        self.typeS = ""
        self.__configVar()

    def __configVar(self):
        text = self.data.split(space)
        for data in text:
            if data in securityType:
                self.flag["security"] = securityType[data]
            elif data == "final":
                self.flag["final"] = data
            elif data == "static":
                self.flag["static"] = data
            else:
                if (data[0] in UPALPHA and not  data[1] in UPALPHA) or "boolean" in data :
                   self.types = data.split('[')[0]
                self.flag["text"] += " " + data

    def toString(self):
        return tab + space.join(self.flag.values()) + ";" + line
