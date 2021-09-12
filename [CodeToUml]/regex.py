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


# arg = {path:str,fatherRep:str,projectName:str,wsdPath:str,code:bool,test:bool,makeFile:bool,jar;dict,readMe:bool}

def runRegex(arg):
    path = re.sub(r"/", separatorR, arg["path"])
    try:
        os.system("mkdir {}{}".format(path+separator,arg["fatherRep"]))
    except Exception as e:
        print(e)
    try:
        os.system("mkdir {}{}src".format(path+separator,arg["fatherRep"]+separator))
    except Exception as e:
        print(e)
    try:
        os.system("mkdir {}{}src{}".format(path+separator,arg["fatherRep"]+separator,separator+arg["projectName"]))
    except Exception as e:
        print(e)
    test = open(arg["wsdPath"] ,"r")
    arg['output'].set("Start Uncode")
    text = test.readline()
    packageData = {arg["projectName"]:{}}
    key = ""
    pack = arg["projectName"]
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
                pack = arg["projectName"]
        elif re.match(implement, text):
            implementListe.append(cleanI(text))
        elif re.match(extends, text):
            extendsListe.append(cleanE(text))
        text = test.readline()
    arg['output'].set("generating pacakge")
    joinData = {"extends":extendsListe,"implements":implementListe}
    packageFinal = []

    for package in packageData:
        thePack = Package(package,package==arg["projectName"])
        for classF in packageData[package]:
            # packageFinal[package].append()
            thePack.addClass(ClassObject(classF, packageData[package][classF]))
        packageFinal.append(thePack)

    arg['output'].set("Writing")
    for package in packageFinal:
        package.joint(joinData)
        package.write(arg["fatherRep"],arg["projectName"],path)

if __name__ == '__main__':
    path = askdirectory() 
    arg = {}
    arg['path'] = path
    arg["fatherRep"] = input("Directory Name >>> ")
    arg["projectName"] = input("projectName >>> ")
    arg["wsdPath"] = input('WSD file path >>> ')
    runRegex(arg)