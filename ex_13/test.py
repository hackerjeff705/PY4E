import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url: ')
html = urllib.request.urlopen(url, context=ctx).read()

tree = ET.fromstring(html)
counts = tree.findall('.//comment')
print('User count:', len(counts))
sum = 0

for values in counts:
    val = int(values.find('count').text)
    sum = sum + val
print(sum)
