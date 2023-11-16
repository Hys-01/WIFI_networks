import subprocess

result = subprocess.run(['netsh', 'wlan', 'show', 'network'], stdout=subprocess.PIPE, text=True)
print(result.stdout)