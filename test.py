import subprocess

# ubprocess.check_output(args, *, stdin=None, stderr=None, shell=False, universal_newlines=False)

args = ['netsh','wlan','show','network']
devices = subprocess.check_output(args=args)


print(devices)