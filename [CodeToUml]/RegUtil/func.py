#!/usr/bin/env python3
# classF file for Function Object
from RegUtil.data import *
import re

class Function:
    def __init__(self, data):
        self.data = data
        self.flag = {
            "com": tab + "/**\n\t* //TODO\n",
            "security": "",
            "static": "",
            "type": "",
            "text": "",
            "end": "",
        }
        self.param = []


        self.__configFunc()


    def __getParam(self,txt):
        txt = txt[1:-1]
        print(txt)
        allParam = txt.split(' , ')
        print(allParam)
        for param in allParam:
            data = param.split(space)
            print(data)
            if len(data)==2:
                self.flag['com'] += tab + "*\n\t* @param " + data[1] + " : "+data[0]+": \n"
    def __configFunc(self):
        param = re.findall(funcParam,self.data)[0]
        self.__getParam(param)
        text = self.data.split(space)
        for data in text:
            if data in securityType:
                self.flag["security"] = tab + securityType[data]
            elif data == "static":
                self.flag["static"] = data
            elif ":" in data:
                dataL = data.split(":")
                self.flag["type"] = dataL[1]
                self.flag["com"] += tab + "*\n\t* @return :" + dataL[1] + ":\n"
                self.flag["text"] += " " + dataL[0]
            else:
                self.flag["text"] += " " + data
            self.flag["end"] = "}"
            if self.flag["type"] == "void" or self.flag["type"] == "":
                self.flag["end"] = ";"
            elif self.flag["type"] in typeReturn:
                self.flag["end"] = "{\n\n\t\t" + typeReturn[self.flag["type"]] + "\n\t}"
            else:
                self.flag["end"] = (
                    "{\n\n\t\treturn new " + self.flag["type"] + "() ;\n\t}"
                )
        self.flag["com"] += tab + "**/" + line

    def toString(self):
        return space.join(self.flag.values()) + line
