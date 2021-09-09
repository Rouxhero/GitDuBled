##!/usr/bin/env python3
# classF file for Variable Object
from data import *


class Variable:
    def __init__(self, data):
        self.data = data
        self.flag = {"security": "", "static": "", "final": "", "text": ""}

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
                self.flag["text"] += " " + data

    def toString(self):
        return space.join(self.flag.values()) + ";" + line
