import subprocess

# ubprocess.check_output(args, *, stdin=None, stderr=None, shell=False, universal_newlines=False)

args = ['netsh','wlan','show','network']
output =  subprocess.check_output(args=args)

# output is a byte-string containing carriagereturn chars and newline chars. 

decodedUTF8 = output.decode('utf-8') 

print(decodedUTF8)
