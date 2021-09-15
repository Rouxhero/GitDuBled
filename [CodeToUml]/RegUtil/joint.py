#!/usr/bin/env python3
# Class for all joint betewn all class
from RegUtil.data import *


class Join:
    def __init__(self, classData: list, jointData: dict):
        self.classData = classData
        self.jointData = jointData

        self.__createJoint()

    def __createJoint(self):
        for key in self.jointData:
            for join in self.jointData[key]:
                if ">" in join:
                    self.__createJointLeft(join, key)
                elif "<" in join:
                    self.__createJointRight(join, key)
                else:
                    print(join)

    def __createJointRight(self, join: str, key: str):
        parts = join.split("<")
        father = parts[0]
        son = parts[1]
        for classO in self.classData:
            if classO.flag["name"] in son:
                classO.flag[key] = key + space + father

    def __createJointLeft(self, join: str, key: str):
        parts = join.split(">")
        father = parts[1]
        son = parts[0]
        for classO in self.classData:
            if classO.flag["name"] in son:
                classO.flag[key] = key + space + father
