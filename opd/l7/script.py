from sys import argv;
from pexpect import spawn;



bcomp = spawn('java -Dmode=cli -jar ../bcomp-ng-ex.jar', encoding='utf-8');
bcomp.sendline(argv[1]);
bcomp.interact()