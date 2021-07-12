import zipfile
import wget
from zipfile import ZipFile
import os
print('Beginning file download with wget module')

url = 'https://github.com/maurosoria/dirsearch/archive/master.zip'
wget.download(url, 'Tools/zip files(delete them when extracted)')

os.makedirs('Tools/dirsearch')


file_name = "Tools/zip files(delete them when extracted)/dirsearch-master.zip"

with zipfile.ZipFile(file_name, 'r') as zip_ref:
    print('Extracting all the files now...')
    zip_ref.extractall('Tools/dirsearch')
    print('Done!')
