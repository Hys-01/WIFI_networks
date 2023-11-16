''' 
Description: 
    This file generates data of networks that can be detected by the device
    The output data shows the number of networks available for the device, and technical information about each one 

Requirements: 
    subprocess, colors_custom and re modules 


'''

# importing necessary modules
import subprocess
from colors_custom import *
import re           # regular expressiosn    # subprocess.check_output(args, *, stdin=None, stderr=None, shell=False, universal_newlines=False)

# retreiving data with args
args = ['netsh','wlan','show','network']
output =  subprocess.check_output(args=args)    # output is a byte-string containing carriagereturn chars and newline chars. 


# decode and clean the data string
decoded_U8 = output.decode('utf-8') 
decoded_U8 = decoded_U8
lines = decoded_U8.split("\r") 

# customization of output, coloring
for i, line in enumerate(lines): 
    # if first line, colour it red and bold the interface name
    if i ==1: 
        titlesplit = lines[i].split(':')
        lines[i] = RED + titlesplit[0] + ":" + BOLD_RED + titlesplit[1] + PLAIN
        
    # if line describing number of networks found, change the number to bold green 
    if line.startswith('\nThere'): 
        # use regex \d to match digits from 0-9
        number = re.findall(r'\d+', line)
        print(number[0])
        lines[i] = re.sub(r'\d+', BOLD_GREEN+str(number[0])+PLAIN, line)

    # if line listing a network, cyan bold the network name
    if line.startswith('\nSSID'): 
        SSIDsplit = line.split(':') 
        lines[i] = SSIDsplit[0] + ':' + BOLD_CYAN + SSIDsplit[1] + PLAIN
        

# after coloring is finished, join the list of strings/lines back into legible format 
final = ' '.join(lines)
print(final)


# remove any active ANSI escape code
print(PLAIN)    





