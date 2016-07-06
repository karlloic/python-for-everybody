# Following Links in Python
import urllib
from BeautifulSoup import *

url = 'http://python-data.dr-chuck.net/known_by_Corrin.html'
itr = int(raw_input('Enter # of iterations: '))
postition = int(raw_input('Enter URL position: '))
urllib.urlop

for i in range(0, itr):
    data = urllib.urlopen(url).read()

    bso = BeautifulSoup(data)
    aTags = bso('a')

    aTag = aTags[postition - 1]
    url = aTag.get('href')
    print(url)
