##!/usr/bin/env python3
# data file for all var
import os

if os.name == "posix":
    separator = '/'
    separatorR = r'/'
else:
    separator = '\\'
    separatorR = r'\\'

    
# Regex
# <|-- Implement
# *--  Extends
endClass = r"}\n"
Var = r"(\+|#)\s?(static)?\s?(final)?\s?[A-Za-z0-9_<>,]+\s[A-Za-z0-9_]+"
Func = r"(\+|#)\s?(static)?\s?([A-Za-z0-9_<>,]+)?\s[A-Za-z0-9_]+(\([A-Za-z0-9_<>,]*\))?(:[A-Za-z0-9_<>,]+)?"
implement = r"([A-Za-z0-9]+)\s?(<\|--|--\|>)\s?([A-Za-z0-9]+)\n"
extends = r"([A-Za-z0-9]+)\s?(\*--|--\*)\s?([A-Za-z0-9]+)\n"
className = r"((abstract\s+)|(protected\s+))?(class|enum|interface)\s+([A-Z][a-zA-Z_]*)(\s+(extends|implement)\s+([A-Z][a-zA-Z_]*))?(\s|\S)+?"
packageR = r'package\s([a-zA-Z_])+\s?\{'

# Var Type

classType = ["class", "interface", "enum"]
classSpe = ["abstract"]
securityType = {"+": "public", "-": "private", "#": "protected"}
typeReturn = {"int": "return 0;", "String": 'return "";'}

# Commun variable

tab = "\t"
space = " "
line = "\n"
author = "/**\n*\n* @author Leo lvcdb, Adrien G\n*/"