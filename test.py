import subprocess

# ubprocess.check_output(args, *, stdin=None, stderr=None, shell=False, universal_newlines=False)

args = ['netsh','wlan','show','network']
output =  subprocess.check_output(args=args)

# output is a byte-string containing carriagereturn chars and newline chars. 

decodedUTF8 = output.decode('utf-8') 

marked = ''
marker_count = 0
numnetworks_notconsidered = True
for x in decodedUTF8:

    if x.isdigit() and numnetworks_notconsidered: 
        marked = marked + "\033[32m" + x + "\033[0m"
        numnetworks_notconsidered = False
        continue


    marked = marked+x  

    if x =="\r": 
        marker_count +=1
        if marker_count ==1: 
            marked = marked + "\033[31m"
        if marker_count==2:
            marked = marked + "\033[0m"

    


print(marked)
