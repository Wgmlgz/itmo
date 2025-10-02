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
	export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:$(current_dir)/src/lib64" && clang -std=c99 -Wall -L. -pedantic *.c -lruntime -o pa3 && \
	./pa3 -p 5 10 10 20 20 30

package:
	rm -rf ./pa3
	mkdir -p ./pa3
	cp -r ./src/. ./pa3/
	tar -cvzf pa3.tar.gz pa3
	rm -rf ./pa3
