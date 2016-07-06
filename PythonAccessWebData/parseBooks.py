import xml.etree.ElementTree as ET

eto = ET.parse("books.xml")
books = eto.findall('books/book')
total = 0
for book in books:
    total += float(book.find('price').text)
print('$'+str(total))
