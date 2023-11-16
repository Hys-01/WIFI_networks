''' 
Description: 
This file generates data of networks that can be detected by the device

'''

import subprocess
from colors_custom import *
import re           # regular expressiosn 
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
        lines[i] = RED + titlesplit[0] + ":" + BOLD_RED + titlesplit[1] + PLAIN
        
    if line.startswith('\nThere'): 
        # use regex \d to match digits from 0-9
        number = re.findall(r'\d+', line)
        print(number[0])
        lines[i] = re.sub(r'\d+', BOLD_GREEN+str(number[0])+PLAIN, line)

    if line.startswith('\nSSID'): 
        SSIDsplit = line.split(':') 
        lines[i] = SSIDsplit[0] + ':' + BOLD_CYAN + SSIDsplit[1] + PLAIN
        

final = ' '.join(lines)
print(final)


print(PLAIN)     # THIS RESETS IT





