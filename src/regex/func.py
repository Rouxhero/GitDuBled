#!/usr/bin/env python3
# classF file for Function Object
from data import *


class Function:
    def __init__(self, data):
        self.data = data
        self.flag = {
            "com": tab+"/**\n\t* auto gen docs\n",
            "security": "",
            "static": "",
            "type": "",
            "text": "",
            "end": "",
        }

        self.__configFunc()

    def __configFunc(self):
        text = self.data.split(space)
        for data in text:
            if data in securityType:
                self.flag["security"] = tab+securityType[data]
            elif data == "static":
                self.flag["static"] = data
            elif ":" in data:
                dataL = data.split(":")
                self.flag["type"] = dataL[1]
                self.flag["com"] += tab+"* @return :" + dataL[1] + ":\n"
                self.flag["text"] += " " + dataL[0]
            else:
                self.flag["text"] += " " + data
            self.flag["end"] = "}"
            if self.flag["type"] == "void" or self.flag['type'] == "":
                self.flag["end"] = ";"
            elif self.flag["type"] in typeReturn:
                self.flag["end"] = "{\n\n\t\t" + typeReturn[self.flag["type"]] + "\n\t}"
            else:
                self.flag["end"] = "{\n\n\t\treturn new " + self.flag["type"] + "() ;\n\t}"
        self.flag["com"] += tab+"**/" + line

    def toString(self):
        return space.join(self.flag.values()) + line
