import zipfile
import wget
from zipfile import ZipFile
import os
print('Beginning file download with wget module')

url = 'https://github.com/radii/msieve/archive/refs/heads/master.zip'
wget.download(url, 'Tools/zip files(delete them when extracted)')

os.makedirs('Tools/msieve')


file_name = "Tools/zip files(delete them when extracted)/msieve-master.zip"

with zipfile.ZipFile(file_name, 'r') as zip_ref:
    print('Extracting all the files now...')
    zip_ref.extractall('Tools/msieve')
    print('Done!')
