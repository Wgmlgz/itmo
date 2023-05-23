#!/bin/bash
cat microcode code.bcomp > start; start | java -Dmode=cli -jar ../bcomp-ng-ex.jar
