import xml.etree.ElementTree as ET

data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
     +1 734 303 4456
   </phone>
   <email hide="yes"/>
</person>'''

parsedData = ET.fromstring(data)
print("Name: " + parsedData.find('name').text)
print("Attr: " + parsedData.find('email').get('hide'))
print(parsedData.find('phone').text.lstrip())

# tree = ET.fromstring(data)
# print 'Name:',tree.find('name').text
# print 'Attr:',tree.find('email').get('hide')
