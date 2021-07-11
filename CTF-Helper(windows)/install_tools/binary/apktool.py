import subprocess
import os
# import sys
import requests
subprocess.call("pip install requests", shell=True)
url = 'https://bitbucket.org/iBotPeaches/apktool/downloads/apktool_2.5.0.jar'
r = requests.get(url, allow_redirects=True)
os.chdir("../../Tools")
open('apktool.jar', 'wb').write(r.content)
# walk_dir = sys.argv[1]
# i = 0
# apktool = "../../Tools/apktool.jar"
# for root, subdirs, files in os.walk(walk_dir):
#     list_file_path = os.path.join(root, 'my-directory-list.txt')
#     with open(list_file_path, 'wb') as list_file:
#         for file in files:
#             if file.endswith(".apk"):
#                 i = 0
#             i = i + 1
#     print(str(i) + "-" + file)
#     os.system("java -jar " + apktool + " d " + root + "/" + file)
#
