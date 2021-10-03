import re
import os
from RegUtil.data import *
from RegUtil.classF import *
from RegUtil.joint import *
from RegUtil.package import *
from RegUtil.makeFile import *
from RegUtil.imports import *
from tkinter.filedialog import *





# arg = {path:str,fatherRep:str,projectName:str,wsdPath:str,makeFile:bool,jar;dict,readMe:bool}


def runRegex(arg):
    path = re.sub(r"/", separatorR, arg["path"])
    try:
        os.system("mkdir {}{}".format(path + separator, arg["fatherRep"]))
    except Exception as e:
        print(e)
    try:
        os.system(
            "mkdir {}{}src".format(path + separator, arg["fatherRep"] + separator)
        )
    except Exception as e:
        print(e)
    try:
        os.system(
            "mkdir {}{}src{}".format(
                path + separator,
                arg["fatherRep"] + separator,
                separator + arg["projectName"],
            )
        )
    except Exception as e:
        print(e)
    print('Creating dir : Done')
    if arg["MakeFile"] and not arg.get("jar", False):
        open(path + separator + arg["fatherRep"] + separator + "Makefile", "w").write(
            MakeFile(arg["projectName"])
        )
    elif arg.get("jar", False):
        open(path + separator + arg["fatherRep"] + separator + "Makefile", "w").write(
            MakeFile(arg["projectName"], jar)
        )
    print('Creating Docs : Done')
    test = open(arg["wsdPath"], "r")
    arg["output"].set("Start Uncode")
    text = test.readline()
    packageData = {arg["projectName"]: {}}
    key = ""
    pack = arg["projectName"]
    implementListe = []
    extendsListe = []
    print('Reading File : Done')
    while text:
        if re.match(packageR, text):
            pack = cleantext(text)
            pack = pack.split(space)[1]
            packageData[pack] = {}
            print(pack)
        elif re.match(className, text):
            key = cleantext(text)
            if pack != "":
                packageData[pack][key] = {"var": [], "func": []}
        elif re.match(Var, text):
            if key != "" and pack != "":
                packageData[pack][key]["var"].append(cleantext(text))
        elif re.match(Func, text):
            if key != "" and pack != "":
                packageData[pack][key]["func"].append(cleantext(text))
        elif re.match(endClass, text):
            if key != "":
                key = ""
            else:
                pack = arg["projectName"]
        elif re.match(implement, text):
            implementListe.append(cleanI(text))
        elif re.match(extends, text):
            extendsListe.append(cleanE(text))
        text = test.readline()
    print('Getting all data : Done')
    arg["output"].set("generating pacakge")
    print(implementListe)
    joinData = {"extends": extendsListe, "implements": implementListe}
    packageFinal = []
    print('Generating package : ')
    for package in packageData:
        thePack = Package(package, package == arg["projectName"])
        print('\tpackage : {}'.format(thePack.name))
        print("-"*20)
        for classF in packageData[package]:
            # packageFinal[package].append()
            print('\t\t'+classF)
            print(packageData[package][classF])
            thePack.addClass(ClassObject(classF, packageData[package][classF]))
            
        packageFinal.append(thePack)
        print("-"*20)
    print('Generating : Done')

    arg["output"].set("Writing")
    aa = Import(packageFinal)
    for package in packageFinal:
        package.joint(joinData)
        package.write(arg["fatherRep"], arg["projectName"], path)


if __name__ == "__main__":
    path = askdirectory()
    arg = {}
    arg["path"] = path
    arg["fatherRep"] = input("Directory Name >>> ")
    arg["projectName"] = input("projectName >>> ")
    arg["wsdPath"] = input("WSD file path >>> ")
    runRegex(arg)
