import subprocess
subprocess.call("pip install requests", shell=True)
import requests
import os
url = 'https://sourceforge.net/projects/dex2jar/files/latest/download'
r = requests.get(url, allow_redirects=True)
os.chdir("../../Tools/dex2jar")
open('dex2jar.zip', 'wb').write(r.content)
# from zipfile import ZipFile
# with ZipFile('dex2jar.zip', 'r') as zipObj:
#     zipObj.extractall()
#
import zipfile
with zipfile.ZipFile("dex2jar.zip", "r") as zip_ref:
    zip_ref.extractall("../../Tools/dex2jar")
