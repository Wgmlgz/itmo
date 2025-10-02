#! TESTED ONLY ON LINUX, but with some changes can probably work on windows

# Project variables
CC := gcc

.PHONY: run

current_dir = $(shell pwd)

run:
	cp -r ../pa1_starter_code/. ./src/
	cp ./src/lib64/libruntime.so ./src/runtime.so
# 	cp -r ../pa2345_starter_code/. ./src/
	cd src && \
	export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:$(current_dir)/src/lib64" && clang -std=c99 -Wall -pedantic *.c -lruntime -o pa2 && \
	./pa2 -p 3 10 20 30

package:
	rm -rf ./pa2
	mkdir -p ./pa2
	cp -r ./src/. ./pa2/
	tar -cvzf pa2.tar.gz pa2
	rm -rf ./pa2
