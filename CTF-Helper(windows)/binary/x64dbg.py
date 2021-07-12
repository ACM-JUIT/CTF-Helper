import zipfile
import wget
from zipfile import ZipFile
import os

print('Beginning file download with wget module')

url = 'https://github.com/x64dbg/x64dbg/releases/download/snapshot/snapshot_2021-07-01_23-17.zip'
wget.download(url, 'Tools/zip files(delete them when extracted)')

os.makedirs('Tools/x64dbg')


file_name = "Tools/zip files(delete them when extracted)/snapshot_2021-07-01_23-17.zip"

with zipfile.ZipFile(file_name, 'r') as zip_ref:
    print('Extracting all the files now...')
    zip_ref.extractall('Tools/x64dbg')
    print('Done!')
