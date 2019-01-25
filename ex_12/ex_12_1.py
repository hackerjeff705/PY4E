import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Set counter to 0
count = 0
sum = 0

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
# Look at the content of span
# Convert each spn into an integer and add it all up
    count = count + 1
    n = int(tag.contents[0])
    sum = sum + n

print(count)
print(sum)
