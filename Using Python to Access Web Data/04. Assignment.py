# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

sum = 0
count = 0
# Retrieve all of the anchor tags
spans = soup.find_all("span")
# print(type(soup))
for span in spans:
    span_value = span.contents[0]
    sum = sum + int(span_value)
    count += 1

print(f'Count {count}')
print(f'Sum {sum}')
