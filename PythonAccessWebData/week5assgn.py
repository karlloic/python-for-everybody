# Extracting Data from XML
import xml.etree.ElementTree as ET
import urllib

data = urllib.urlopen("http://python-data.dr-chuck.net/comments_279057.xml").read()
eto = ET.fromstring(data)

counts = eto.findall(".//count")
total = 0
for count in counts:
    total += int(count.text)

print(total)
