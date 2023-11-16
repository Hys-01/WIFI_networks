import subprocess

result = subprocess.run(['netsh', 'wlan', 'show', 'network'], stdout=subprocess.PIPE, text=True)
print(result.stdout)


if output.returncode == 0:
    result = output.stdout
    lines = result.split("\n") 
    print(lines)