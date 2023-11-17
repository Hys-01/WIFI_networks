import subprocess

result = subprocess.run(['netsh', 'wlan', 'show', 'network'], stdout=subprocess.PIPE, text=True)
print(result.stdout)


if output.returncode == 0:
    result = output.stdout
    lines = result.split("\n") 
    print(lines)

try:
    subprocess.run(["C:\\Users\\hbros\\WlanScan.exe"], check=True)
except subprocess.CalledProcessError as e:
    print(f"Error running WlanScan.exe: {e}")
else:
    print("Wi-Fi rescan triggered successfully.")