import subprocess
from colors_custom import *
# ubprocess.check_output(args, *, stdin=None, stderr=None, shell=False, universal_newlines=False)

args = ['netsh','wlan','show','network']
output =  subprocess.check_output(args=args)

# output is a byte-string containing carriagereturn chars and newline chars. 

decoded_U8 = output.decode('utf-8') 
decoded_U8 = decoded_U8
lines = decoded_U8.split("\r") 

print(lines)
print(PLAIN)





