##!/usr/bin/env python3
# data file for all var
import os

if os.name == "posix":
    separator = "/"
    separatorR = r"/"
else:
    separator = "\\"
    separatorR = r"\\"

def clearSpace(text):
    for n in range(2,10):   
        text = text.replace(" "*n," ")
    return text
# Regex
# <|-- Implement
# *--  Extends
endClass = r"}\n"
Var = r"^\t*(\+|#|-)\s?(static)?\s?(final)?\s?[A-Za-z0-9_<>,\[\]]*\s[A-Za-z0-9_]+\n?$"
Func = r"^\t*(\+|#|-)\s?(\{abstract\})?\s?(static)?\s?([A-Za-z0-9_<>,]+)?\s[A-Za-z0-9_]+\([A-Za-z0-9_<>, ]*\)(:[A-Za-z0-9_<>,]+)?"
extends = r"^\t*([A-Za-z0-9]+)\s?(<\|--|--\|>)\s?([A-Za-z0-9]+)\n"
implement = r"^\t*([A-Za-z0-9]+)\s?(\*--|--\*)\s?([A-Za-z0-9]+)\n"
className = r"^\t*((abstract\s+)|(protected\s+))?(class|enum|interface)\s+([A-Z][a-zA-Z_]*)(\s+(extends|implement)\s+([A-Z][a-zA-Z_]*))?(\s|\S)+?"
packageR = r"^\t*package\s([a-zA-Z_])+\s?\{"
funcParam = r'\([\w,\s<>_]*\)'
folderCreate = r'[a-zA-Z0-9_\s\(\)\[\]]+$'
# Var Type

classType = ["class", "interface", "enum"]
classSpe = ["abstract"]
securityType = {"+": "public", "-": "private", "#": "protected"}
typeReturn = {"int": "return 0;", "String": 'return "";', "boolean":"return true;"}

# Commun variable

tab = "\t"
space = " "
line = "\n"
author = "/**\n*\n* @author Leo lvcdb, Adrien G\n*/"
