import urllib

fhand = urllib.urlopen('http://www.py4inf.com/codes/romeo.txt')
for line in fhand:
    print line.strip()

