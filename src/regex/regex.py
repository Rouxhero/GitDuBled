import re
from data import *
from classF import *

# Code fini :
test = open("test.wsd", "r")
text = test.readline()
data = {}
key = ""


def cleantext(text):
    text = re.sub("\n", "", text)
    text = re.sub("{", "", text)
    return text


while text:
    if re.match(className, text):
        key = cleantext(text)
        data[key] = {"var": [], "func": []}
    elif re.match(Var, text):
        if key != "":
            data[key]["var"].append(cleantext(text))
    elif re.match(Func, text):
        if key != "":
            data[key]["func"].append(cleantext(text))
    elif re.match(endClass, text):
        key = ""
    text = test.readline()

print(data)
classListe = []

for classF in data:
    classListe.append(ClassObject(classF, data[classF]))
    # alls  = classF.split(' ')
    # name  = ""
    # typeD = ""
    # Spe   = ""
    # for d in alls:
    # 	if d in classType:
    # 		typeD = d
    # 	elif d in classSpe :
    # 		Spe   = d
    # 	else :
    # 		name = d
    # classHead = Spe+" "+typeD+" "+name+" {\n\n"
    # print(classHead)
    # allVar = ""
    # security = ""
    # static   = False
    # final    = False
    # lastT    = ""
    # for var in data[classF]['var']:
    # 	text = var.split(' ')
    # 	security = ""
    # 	static   = False
    # 	final    = False
    # 	lastT    = ""
    # 	for txt in text:
    # 		if txt in securityType:
    # 			security = securityType[txt]
    # 		elif txt == "final":
    # 			final = True
    # 		elif txt == "static":
    # 			static = True
    # 		else :
    # 			lastT += " "+txt
    # 	allVar += "\t"+security+staticD[static]+finalD[final]+lastT+";\n"
    # # print(allVar)
    # allFunc = ""
    # security = ""
    # static   = False
    # final    = False
    # lastT    = ""
    # types    = ""
    # com 	 = ""
    # for func in data[classF]['func']:
    # 	text = func.split(' ')
    # 	security = ""
    # 	static   = False
    # 	final    = False
    # 	lastT    = ""
    # 	types    = ""
    # 	com 	 = "/**\n\t* def\n\t"
    # 	for txt in text:
    # 		if txt in securityType:
    # 			security = securityType[txt]
    # 		elif txt == "final":
    # 			final = True
    # 		elif txt == "static":
    # 			static = True
    # 		elif ":" in txt:
    # 			txt = txt.split(":")
    # 			print(txt)
    # 			types = txt[1]
    # 			com+= "* @return :"+txt[1]+":\n\t"
    # 			lastT += " "+txt[0]
    # 		else :
    # 			lastT += " "+txt
    # 		end = "}"
    # 		if types == "void":
    # 			end = ";"
    # 		elif types in typeReturn:
    # 			end = "{\n\n\t\t"+typeReturn[types]+"\n\t}"
    # 		else :
    # 			end = "{\n\n\t\treturn new "+types+";\n\t}"
    # 	allFunc += "\t"+com+"**/\n\t"+security+staticD[static]+finalD[final]+" "+types+lastT+end+"\n\n"
    # print(allFunc)
    # open("javaFile/"+name+".java","w+").write(classHead+allVar+allFunc+"\n}")

for classO in classListe:
    print(classO.toString())
