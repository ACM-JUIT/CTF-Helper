import wget
from zipfile import ZipFile
import os

print('Beginning file download with wget module')
os.makedirs('Tools/burpsuite')

url = 'https://portswigger.net/burp/releases/download?product=community&version=2021.6.2&type=WindowsX64'
wget.download(url, 'Tools/burpsuite')

# os.startfile("C:\Users\ASUS\Documents\cyber projects\CTF-Helper\CTF-Helper(windows)\Tools\burpsuite\burpsuite_community_windows-x64_v2021_6_2.exe")
