import subprocess
from colors_custom import *
# ubprocess.check_output(args, *, stdin=None, stderr=None, shell=False, universal_newlines=False)

args = ['netsh','wlan','show','network']
output =  subprocess.check_output(args=args)

# output is a byte-string containing carriagereturn chars and newline chars. 

decoded_U8 = output.decode('utf-8') 
decoded_U8 = decoded_U8
lines = decoded_U8.split("\r") 

for i, line in enumerate(lines): 
    if i ==1: 
        titlesplit = lines[i].split(':')
        print(titlesplit)
        lines[i] = RED + titlesplit[0] + BOLD_RED + titlesplit[1] 

final = ' '.join(lines)
print(final)




print(PLAIN)     # THIS RESETS IT





