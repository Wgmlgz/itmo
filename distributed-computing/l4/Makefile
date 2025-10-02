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
	export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:$(current_dir)/src/lib64" && clang -std=c99 -Wall -L. -pedantic *.c -lruntime -o pa4 && \
	./pa4 -p 3 --mutexl

package:
	rm -rf ./pa4
	mkdir -p ./pa4
	cp -r ./src/. ./pa4/
	tar -cvzf pa4.tar.gz pa4
	rm -rf ./pa4
