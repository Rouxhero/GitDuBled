import re
import os
from data import *
from classF import *
from joint import *
from package import *


fatherRep = input("Directory Name >>> ")
projectName = input("ProjectName >>> ")
os.system("mkdir {}".format(fatherRep))
os.system("mkdir {}/src".format(fatherRep))
os.system("mkdir {}/src/{}".format(fatherRep,projectName))
wsdPath = input('WSD file path >>> ')
test = open(wsdPath ,"r")
text = test.readline()
packageData = {projectName:{}}
key = ""
pack = projectName
implementListe = []
extendsListe = []

def cleantext(text):
    text = re.sub("\n", "", text)
    text = re.sub("{", "", text)
    return text


def cleanI(text):
    text = re.sub(r"<\|--", "<", text)
    text = re.sub(r"--\|>", ">", text)
    return cleantext(text)

def cleanE(text):
    text = re.sub(r"\*--", "<", text)
    text = re.sub(r"--\*", ">", text)
    return cleantext(text)

while text:
    if re.match(package,text):
        pack = cleantext(text)
        pack = pack.split(space)[1]
        packageData[pack] = {}
        print(pack)
    elif re.match(className, text):
        key = cleantext(text)
        if pack != "":
            packageData[pack][key] = {"var": [], "func": []}
    elif re.match(Var, text):
        if key != "" and pack !="":
            packageData[pack][key]["var"].append(cleantext(text))
    elif re.match(Func, text):
        if key != "" and pack !="":
            packageData[pack][key]["func"].append(cleantext(text))
    elif re.match(endClass, text):
        if key != "":
            key = ""
        else :
            pack = projectName
    elif re.match(implement, text):
        implementListe.append(cleanI(text))
    elif re.match(extends, text):
        extendsListe.append(cleanE(text))


    text = test.readline()

joinData = {"extends":extendsListe,"implement":implementListe}
packageFinal = []

for package in packageData:
    thePack = Package(package,package==projectName)
    for classF in packageData[package]:
        # packageFinal[package].append()
        thePack.addClass(ClassObject(classF, packageData[package][classF]))
    packageFinal.append(thePack)


for package in packageFinal:
    package.joint(joinData)
    package.write(fatherRep,projectName)
