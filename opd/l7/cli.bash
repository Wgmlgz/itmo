#!/bin/bash
cat microcode > start;
echo "asm" >> start;
cat code.bcomp >> start;
echo "" >> start;
echo "END" >> start;
echo "ru" >> start;
echo "s" >> start;

echo "a 221" > end;
echo "r" >> end;


# cat start | java -Dmode=cli -jar ../bcomp-ng-ex.jar
# cat start | xargs python script.py
