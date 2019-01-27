import urllib.request, urllib.parse, urllib.error
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
print('Retrieving', url)

html = urllib.request.urlopen(url, context=ctx).read()
info = json.loads(html)
print('Retrieved', len(html), 'characters')

comments = info['comments']
print('Count:', len(comments))
tot = 0

for count in comments:
    val = int(count['count'])
    tot = tot + val

print(tot)
