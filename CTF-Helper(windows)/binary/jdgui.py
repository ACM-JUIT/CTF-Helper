import zipfile
import wget
from zipfile import ZipFile
import os
print('Beginning file download with wget module')

url = 'https://github.com/java-decompiler/jd-gui/releases/download/v1.6.6/jd-gui-windows-1.6.6.zip'
wget.download(url, 'Tools/zip files(delete them when extracted)')

os.makedirs('Tools/jdgui')


file_name = "Tools/zip files(delete them when extracted)/jd-gui-windows-1.6.6.zip"

with zipfile.ZipFile(file_name, 'r') as zip_ref:
    print('Extracting all the files now...')
    zip_ref.extractall('Tools/jdgui')
    print('Done!')
