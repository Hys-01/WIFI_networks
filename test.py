import subprocess

# ubprocess.check_output(args, *, stdin=None, stderr=None, shell=False, universal_newlines=False)

args = ['netsh','wlan','show','network']
output =  subprocess.check_output(args=args)
print(output)
# output is a byte-string containing carriagereturn chars and newline chars. 

decodedUTF8 = output.decode('utf-8') 

marked = ''
marker_count = 0
for x in decodedUTF8: 
    marked = marked+x

    if x =="\r": 
        marker_count +=1
        print('aaa')
        if marker_count %2 ==1: 
            marked = marked + "\033[31m"
        else: 
            marked = marked + "\033[0m"
    


print(marked)
