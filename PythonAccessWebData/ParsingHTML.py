# Scraping an html page
import urllib
from BeautifulSoup import *

data = urllib.urlopen("http://www.py4inf.com/book.htm").read()
parsedHTML = BeautifulSoup(data)
tags = parsedHTML('a')


for tag in tags:
    print 'URL:', tag.get('href', None)
    print 'Content:', tag.contents[0]
    print 'Attributes:', tag.attrs
