''' 
Description: 
    This file generates data of networks that can be detected by the device
    The output data shows the number of networks available for the device, and technical information about each one 

Requirements: 
    subprocess and re modules 

'''

# importing necessary modules
import subprocess
from colors_custom import *
from formatting import decode, colorize
# retreiving data with args
args = ['netsh','wlan','show','network']
output =  subprocess.check_output(args=args)    # output is a byte-string containing carriagereturn chars and newline chars. 

lines = decode(output)
final = colorize(lines)


# remove any active ANSI escape code
print(PLAIN)    





