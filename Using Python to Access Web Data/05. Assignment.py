# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

URL = input("Enter the URL:") 
link_line = int(input("Enter position:")) - 1 
count = int(input("Enter count:")) 

while count >= 0:
    html = urllib.request.urlopen(URL).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    print(URL)
    URL = tags[link_line].get("href", None)
    count = count - 1