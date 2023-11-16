''' 
Description: 
    This file generates data of networks that can be detected by the device
    The output data shows the number of networks available for the device, and technical information about each one
    THe data is formatted/stylized using functions from formatting.py 

Requirements: 
    subprocess and re and formatting modules


'''

# importing necessary modules
import subprocess
from colors_custom import *
from formatting import decode, colorize
# retreiving data with args
args = ['netsh','wlan','show','network']
output =  subprocess.check_output(args=args)    # output is a byte-string containing carriagereturn chars and newline chars. 

# format the data using formatting.py
lines = decode(output)
final = colorize(lines)


# remove any active ANSI escape code
print(PLAIN)    





