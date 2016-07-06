# Chapter 12.8 Exercise 12.1
import urllib
from BeautifulSoup import *

url = 'http://www.cnn.com'
content = urllib.urlopen(url).read()

bso = BeautifulSoup(content)
ptags = bso('p')

print('The URL \'' + url + '\' contains ' + str(len(ptags)) + ' paragraphs')
