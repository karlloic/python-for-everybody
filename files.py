# Look for lines with style New Revision: 39772
# TODO Test
import re
fhandle = open("mbox.txt")
search = raw_input("Enter regular expression: ")
count = 0
for line in fhandle:
    found = re.findall(search, line)
    if found:
        count += 1
print "mbox.txt has", count, "matching the expression", search


