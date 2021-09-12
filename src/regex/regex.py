import re
import os
from RegUtil.data import *
from RegUtil.classF import *
from RegUtil.joint import *
from RegUtil.package import *
from tkinter.filedialog import *



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



def runRegex(path,fatherRep,projectName,wsdPath):
    path = re.sub(r"/", separatorR, path)
    os.system("mkdir {}{}".format(path+separator,fatherRep))
    os.system("mkdir {}{}src".format(path+separator,fatherRep+separator))
    os.system("mkdir {}{}src{}".format(path+separator,fatherRep+separator,separator+projectName))
    test = open(wsdPath ,"r")
    text = test.readline()
    packageData = {projectName:{}}
    key = ""
    pack = projectName
    implementListe = []
    extendsListe = []
    while text:
        if re.match(packageR,text):
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

    joinData = {"extends":extendsListe,"implements":implementListe}
    packageFinal = []

    for package in packageData:
        thePack = Package(package,package==projectName)
        for classF in packageData[package]:
            # packageFinal[package].append()
            thePack.addClass(ClassObject(classF, packageData[package][classF]))
        packageFinal.append(thePack)


    for package in packageFinal:
        package.joint(joinData)
        package.write(fatherRep,projectName,path)

if __name__ == '__main__':
    path = askdirectory() 
    fatherRep = input("Directory Name >>> ")
    projectName = input("ProjectName >>> ")
    wsdPath = input('WSD file path >>> ')
    runRegex(path,fatherRep,projectName,wsdPath)