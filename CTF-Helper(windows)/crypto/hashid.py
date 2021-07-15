import zipfile
import wget
from zipfile import ZipFile
import os
print('Beginning file download with wget module')

url = 'https://github.com/psypanda/hashID/zipball/master'
wget.download(url, 'Tools/zip files(delete them when extracted)')

os.makedirs('Tools/hashid')


file_name = "Tools/zip files(delete them when extracted)/psypanda-hashID-v3.1.4-16-g7e8473a.zip"

with zipfile.ZipFile(file_name, 'r') as zip_ref:
    print('Extracting all the files now...')
    zip_ref.extractall('Tools/hashid')
    print('Done!')
