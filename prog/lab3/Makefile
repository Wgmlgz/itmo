out = lab3.jar

all: clean run

clean :
	rm -f `find . -name *.class` $(out)

classes:
	javac -d build `find . -name *.java`

jar: classes
	cd build; jar cfm ../$(out) ../manifest.mf `find . -name *.class`

run: jar
	java -jar $(out)

dump: jar
	java -jar $(out) > out.txt


