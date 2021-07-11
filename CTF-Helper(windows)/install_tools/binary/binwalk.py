import subprocess
import git
import os
import sys
# import binwalk
subprocess.call("pip install pylzma", shell=True)
subprocess.call("pip install gitpython", shell=True)
git.Git("../../Tools").clone("https://github.com/ReFirmLabs/binwalk.git")
subprocess.call("pip install binwalk", shell=True)
subprocess.call("python setup.py install", shell=True)
strl = ''.join(sys.argv[1:])
command = "../../Tools"+strl
os.system(command)
subprocess.call("python install pyinstaller", shell=True)
subprocess.call("pyinstaller --onefile binwalk.py", shell=True)
