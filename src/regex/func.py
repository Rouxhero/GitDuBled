#!/usr/bin/env python3
# classF file for Function Object
from data import *


class Function:
    def __init__(self, data):
        self.data = data
        self.flag = {
            "com": "/**\n* auto gen docs\n",
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
                self.flag["security"] = securityType[data]
            elif data == "static":
                self.flag["static"] = data
            elif ":" in data:
                dataL = data.split(":")
                self.flag["types"] = dataL[1]
                self.flag["com"] += "* @return :" + dataL[1] + ":\n\t"
                self.flag["text"] += " " + dataL[0]
            else:
                self.flag["text"] += " " + data
            self.flag["end"] = "}"
            if self.flag["type"] == "void":
                self.flag["end"] = ";"
            elif self.flag["type"] in typeReturn:
                self.flag["end"] = "{\n\n\t\t" + typeReturn[self.flag["type"]] + "\n\t}"
            else:
                self.flag["end"] = "{\n\n\t\treturn new " + self.flag["type"] + ";\n\t}"
        self.flag["com"] += "**/" + line

    def toString(self):
        return space.join(self.flag.values()) + line
