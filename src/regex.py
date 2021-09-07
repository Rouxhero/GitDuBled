import re

# Code fini :
endClass = r'}\n'
Var = r'(\+|#)\s?[A-Za-z0-9_<>,]+\s(static)?\s?(final)?\s?[A-Za-z0-9_]+\n'
Func = r'(\+|#)+\s+(\d|\w)+[(]+((\d|\w|\s)*)+?\W+((\d|\w|\s))[^\n]+'
heritage = r'([A-Za-z0-9]+)\s?(<\|--|--\|>)\s?([A-Za-z0-9]+)\n'
className = r'((abstract\s+)|(protected\s+))?(class|enum|interface)\s+([A-Z][a-zA-Z_]*)(\s+(extends|implement)\s+([A-Z][a-zA-Z_]*))?(\s|\S)+?'
line = r'((abstract\s+)|(protected\s+))?(class|enum|interface)\s+([A-Z][a-zA-Z_]*)(\s+(extends|implement)\s+([A-Z][a-zA-Z_]*))?(\s|\S)+?'
test = open("test.wsd",'r')
text = test.readline()
data = {}
key = ""

def cleantext(text):
	text = re.sub("\n","",text)
	text = re.sub("{","",text)
	return text

while text :
	if re.match(className, text) :
		key = cleantext(text)
		data[key] = []
	elif re.match(Var,text) or re.match(Func,text)  :
		if key != '':
			data[key].append(cleantext(text))
	elif re.match(endClass,text) :
		key = ''
	text = test.readline()

print(data)

