import zipfile
import wget
from zipfile import ZipFile
import os
import sys

print('Beginning file download with wget module')
#subprocess.call("pip install pylzma", shell=True)

url = 'https://github.com/ReFirmLabs/binwalk/archive/refs/tags/v2.2.0.zip'
wget.download(url, 'Tools/zip files(delete them when extracted)')

os.makedirs('Tools/binwalk')

file_name = "Tools/zip files(delete them when extracted)/binwalk-2.2.0.zip"
with zipfile.ZipFile(file_name, 'r') as zip_ref:
    print('Extracting all the files now...')
    zip_ref.extractall('Tools/binwalk')

#subprocess.call("python setup.py install", shell=True)
#subprocess.call("python setup.py install", shell=True)
