# Extracting Data from JSON

import urllib
import json

data = urllib.urlopen("http://python-data.dr-chuck.net/comments_279061.json").read()

if len(data) < 1:
    print("Enter valid URL")
    exit()
print("Retrieved" + str(len(data)) + " characters")
parsedData = json.loads(data)
print(json.dumps(parsedData, indent=4))

total = 0
for comment in parsedData["comments"]:
    total += comment["count"]

print(total)
