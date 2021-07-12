import zipfile
import wget
from zipfile import ZipFile
import os

print('Beginning file download with wget module')

url = 'https://github.com/raddyfiy/xortool-for-Windows/releases/download/0.98w/xortool_0.98win.zip'
wget.download(url, 'Tools/zip files(delete them when extracted)')

os.makedirs('Tools/xortool')


file_name = "Tools/zip files(delete them when extracted)/xortool_0.98win.zip"

with zipfile.ZipFile(file_name, 'r') as zip_ref:
    print('Extracting all the files now...')
    zip_ref.extractall('Tools/xortool')
    print('Done!')
