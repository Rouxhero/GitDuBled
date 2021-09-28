
PROJECT=t1

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
	rm -rf $(OUT)