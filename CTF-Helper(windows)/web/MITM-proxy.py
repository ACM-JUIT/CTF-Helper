import wget
from zipfile import ZipFile
import os

print('Beginning file download with wget module')
os.makedirs('Tools/MITM-proxy')

url = 'https://snapshots.mitmproxy.org/6.0.2/mitmproxy-6.0.2-windows-installer.exe'
wget.download(url, 'Tools/MITM-proxy')
