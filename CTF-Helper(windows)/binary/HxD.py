import zipfile
import wget
from zipfile import ZipFile
import os

print('Beginning file download with wget module')

url = 'https://download.heise.de/files/LkKxKFGn965sB5uwUr4QWg/281643/hxdsetup.zip?expires=1626087929'
wget.download(url, 'Tools/zip files(delete them when extracted)')

os.makedirs('Tools/HxD')


file_name = "Tools/zip files(delete them when extracted)/hxdsetup.zip"

with zipfile.ZipFile(file_name, 'r') as zip_ref:
    print('Extracting all the files now...')
    zip_ref.extractall('Tools/HxD')
    print('Done!')
