JAVAC=javac
sources = $(wildcard *.java)
classes = $(sources:.java=.class)

all: run

clean :
	rm -f *.class *.jar

%.class : %.java
	$(JAVAC) $<

jar: $(classes)
	jar -cvfm lab1.jar manifest.mf $(classes) 

run: jar
	java -jar lab1.jar
