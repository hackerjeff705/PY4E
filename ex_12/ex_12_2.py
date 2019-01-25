import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url: ')
count = int(input('Enter count: '))
pos = int(input('Enter position: '))
count_n = 0

for html in url:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    pos_n = 1

    for tag in tags:

        if count_n == 0:
            start_txt = url.find('by_')
            end_txt = url.find('.html')
            print(url[start_txt+3:end_txt])
            count_n = count_n + 1

        elif pos_n == pos:
            print(tag.contents[0])
            url = tag.get('href', None)
            count_n = count_n + 1

        elif count_n > count:
            break

        pos_n = pos_n + 1
