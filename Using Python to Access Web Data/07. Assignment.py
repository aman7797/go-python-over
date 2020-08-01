
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

URL = input("Enter location:") 
# URL = 'http://py4e-data.dr-chuck.net/comments_702805.xml'
print('Retrieved', len(URL), 'characters')
sum = 0
xml = urllib.request.urlopen(URL).read()
content = ET.fromstring(xml)
countlst = content.findall('.//count')
print(f'Count: {len(countlst)}')
for elem in countlst:
    sum += int(elem.text)

print(f'Sum: {sum}')