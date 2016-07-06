# Download and print file content
import urllib
fhandle = urllib.urlopen("http://www.py4inf.com/codes/romeo.txt")

for line in fhandle:
    print(line.strip())
