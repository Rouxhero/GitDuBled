# #!/usr/bin/env python3

MakeFileJar = lambda jar,projectName :"""
PROJECT={}

BUILD=javac
RUN =jar
DOCS = javadoc
OUT ?= classes/
JAR ?= jar/
DOC ?= docs/

ARGJAR=-c -v -f  $(JAR)$@


FILE = $(wildcard src/$(PROJECT)/*.java src/$(PROJECT)/*/*.java)

{}.jar : cls 
	$(RUN) $(ARGJAR) -e $(PROJECT).{} -C $(OUT) $(PROJECT)

cls :
	$(BUILD) -d $(OUT)  $(FILE)

doc:
	$(DOCS) -d $(DOC) $(FILE)

clean:
	rm -rf $(OUT)""".format(projectName,jar['name'],jar['main'])


def MakeFile(projectName,jar=False):

	if not jar :
		return """
PROJECT={}

BUILD=javac
RUN =jar
DOCS = javadoc
OUT ?= classes/
JAR ?= jar/
DOC ?= docs/

FILE = $(wildcard src/$(PROJECT)/*.java src/$(PROJECT)/*/*.java)

cls :
	$(BUILD) -d $(OUT)  $(FILE)

doc:
	$(DOCS) -d $(DOC) $(FILE)

clean:
	rm -rf $(OUT)""".format(projectName)
	else :
		return MakeFileJar(jar,projectName) 