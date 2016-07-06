# Scraping Numbers from HTML using BeautifulSoup
import urllib
from BeautifulSoup import *

content = urllib.urlopen('http://python-data.dr-chuck.net/comments_279060.html').read()
bso = BeautifulSoup(content)

spanTags = bso('span')
total = 0
for spanTag in spanTags:
    total += int(spanTag.contents[0])

print('Count ' + str(len(spanTags)))
print('Sum ' + str(total))
print(type(spanTag.contents[0]))
