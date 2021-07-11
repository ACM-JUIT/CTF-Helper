import subprocess
subprocess.call("pip install requests", shell=True)
import requests
import os
url = 'https://filehippo.com/download_hxd-hex-editor/post_download/'
r = requests.get(url, allow_redirects=True)
os.chdir("../../Tools/HxD")
open('HxD.zip', 'wb').write(r.content)
from zipfile import ZipFile
with ZipFile('HxD.zip', 'r') as zipobj:
    zipobj.extractall()