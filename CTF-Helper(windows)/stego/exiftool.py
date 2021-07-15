import zipfile
import wget
from zipfile import ZipFile
import os
print('Beginning file download with wget module')

url = 'https://exiftool.org/exiftool-12.29.zip'
wget.download(url, 'Tools/zip files(delete them when extracted)')

os.makedirs('Tools/exiftool')

file_name = "Tools/zip files(delete them when extracted)/exiftool-12.29.zip"
with zipfile.ZipFile(file_name, 'r') as zip_ref:
    print('Extracting all the files now...')
    zip_ref.extractall('Tools/exiftool')
    print('Done!')
