JAVAC = javac
sources = $(wildcard *.java)
classes = $(sources:.java=.class)
out = lab2.jar

all: clean run

clean :
	rm -f *.class *.jar

%.class : %.java
	$(JAVAC) $<

classes:
	javac -cp lib/Pokemon.jar -d . `find . -name *.java`

jar: classes
	jar cfm $(out) manifest.mf `find . -name *.class`

run: jar
	java -jar $(out)


