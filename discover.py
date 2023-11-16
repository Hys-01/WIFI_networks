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
from formatting import colorize
# retreiving data with args
args = ['netsh','wlan','show','network']
output =  subprocess.run(args=args, capture_output=True, text=True)    # output is a byte-string containing carriagereturn chars and newline chars. 

# format the data using formatting.py
if output.returncode == 0:
    result = output.stdout
    lines = result.split("\n") 

    final = colorize(lines)
    print(final)

else:
    print("Error executing command:", output.stderr)



# remove any active ANSI escape code
print(PLAIN)    




'''
future plans: 
emphasise the network currently connected (if any connected at all) 
note LOCKED/PASSWORD networks to guest/unlocked ones 
ADD NEW ATTRIBUTE dBM for signal STRENGTH (quantifier of wifi bars) 
'''





