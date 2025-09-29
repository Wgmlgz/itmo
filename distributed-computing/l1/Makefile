#! TESTED ONLY ON LINUX, but with some changes can probably work on windows

# Project variables
CC := gcc

.PHONY: run


run:
	cp -r ../pa1_starter_code/. ./src/
	cd src && \
	clang -std=c99 -Wall -pedantic *.c -o main && \
	./main -p 4

package:
	rm -rf ./pa1
	mkdir -p ./pa1
	cp -r ./src/. ./pa1/
	tar -cvzf pa1.tar.gz pa1