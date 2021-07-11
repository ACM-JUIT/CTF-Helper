import subprocess
import os
import requests
subprocess.call("pip install requests", shell=True)
url = 'https://out7.hex-rays.com/files/idafree76_windows.exe'
r = requests.get(url, allow_redirects=True)
os.chdir("../../Tools/idafree")
open('idafree.exe', 'wb').write(r.content)
os.startfile("C:\Users\Haripriya Radhika\CTF-Helper\CTF-Helper(windows)\Tools\idafree.exe")
os.system("C:\Users\Haripriya Radhika\CTF-Helper\CTF-Helper(windows)\Tools\idafree.exe")