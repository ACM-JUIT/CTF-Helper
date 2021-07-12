import zipfile
import wget
from zipfile import ZipFile
import os


print('Beginning file download with wget module')

url = 'https://github.com/pxb1988/dex2jar/releases/download/2.0/dex-tools-2.0.zip'
wget.download(url, 'Tools/zip files(delete them when extracted)')

os.makedirs('Tools/dex2jar')


file_name = "Tools/zip files(delete them when extracted)/dex-tools-2.0.zip"

with zipfile.ZipFile(file_name, 'r') as zip_ref:
    print('Extracting all the files now...')
    zip_ref.extractall('Tools/dex2jar')
    print('Done!')
