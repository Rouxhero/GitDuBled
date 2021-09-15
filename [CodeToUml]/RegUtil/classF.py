##!/usr/bin/env python3
# File for classObject
from RegUtil.data import *
from RegUtil.var import *
from RegUtil.func import *

# Class for classObject


class ClassObject:
    def __init__(self, head, data):
        self.head = head
        self.data = data
        self.flag = {
            "spec": "",
            "type": "",
            "name": "",
            "implements": "",
            "extends": "",
        }
        self.var = []
        self.func = []
        self.__configClass()
        self.__configVariable()
        self.__configFunction()

    def __configClass(self):
        print(tab*3+'Config name')
        data = self.head.split(space)
        for text in data:
            if text in classType:
                self.flag["type"] = text
            elif text in classSpe:
                self.flag["spec"] = text
            else:
                self.flag["name"] = text

    def __configVariable(self):
        for var in self.data["var"]:
            self.var.append(Variable(var))
            print(tab*3+'var :'+self.var[-1].flag['text'])

    def __configFunction(self):
        for func in self.data["func"]:
            self.func.append(Function(func))

    def toString(self):
        varT = ""
        for var in self.var:
            varT += var.toString() + line

        funcT = ""
        for func in self.func:
            funcT += func.toString() + line
        return (
            space.join(self.flag.values())
            + "{"
            + line * 2
            + varT
            + line
            + funcT
            + line
            + "}"
        )
