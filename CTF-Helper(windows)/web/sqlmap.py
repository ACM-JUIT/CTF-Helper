import zipfile
import wget
from zipfile import ZipFile
import os
print('Beginning file download with wget module')

url = 'https://github.com/sqlmapproject/sqlmap/zipball/master'
wget.download(url, 'Tools/zip files(delete them when extracted)')

os.makedirs('Tools/sqlmap')


file_name = "Tools/zip files(delete them when extracted)/sqlmapproject-sqlmap-1.5.7-2-g795b9e6.zip"

with zipfile.ZipFile(file_name, 'r') as zip_ref:
    print('Extracting all the files now...')
    zip_ref.extractall('Tools/sqlmap')
    print('Done!')
