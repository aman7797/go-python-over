
import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# URL = input("Enter location:") 
URL = 'http://py4e-data.dr-chuck.net/comments_702806.json'
print('Retrieved', URL)
sum = 0
data = urllib.request.urlopen(URL).read().decode()
jsonParse = json.loads(data)
comments = jsonParse['comments']
print(f'Count: {len(comments)}')
for item in comments:
    # print(item)
    sum += item['count']
print(f'Sum: {sum}')

