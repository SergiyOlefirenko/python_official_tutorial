import urllib.request
from bs4 import BeautifulSoup


url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# return all ancor tags
tags = soup('a')
print(tags)
for tag in tags:
    print(tag.get('href', None))
