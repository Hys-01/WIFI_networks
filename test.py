import subprocess

# ubprocess.check_output(args, *, stdin=None, stderr=None, shell=False, universal_newlines=False)

args = ['netsh','wlan','show','network']
output =  subprocess.check_output(args=args)

# output is a byte-string containing carriagereturn chars and newline chars. 
print(output)
decodedUTF8 = output.decode('utf-8') 

print(decodedUTF8)

marked = ''
marker_count = 0
for x in decodedUTF8: 
    marked = marked+x

    if x =="\r": 
        marker_count +=1
        marked = marked+ ('$' + str(marker_count))


print(marked)
