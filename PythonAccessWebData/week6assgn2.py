# Calling a JSON API

import urllib
import json

location = raw_input("Enter a location: ")
endpoint = "http://python-data.dr-chuck.net/geojson"
urlParam = urllib.urlencode({"sensor": "false", "address": location})
url = endpoint + "?" + urlParam

data = urllib.urlopen(url).read()
if len(data) < 1:
    print("Enter valid URL")
    exit()

try:
    parsedData = json.loads(data)
except:
    print("Invalid location: ")
    exit()

if parsedData["status"] != "OK" or "status" not in parsedData:
    print("Unable to retrieve data")
    exit()

print(parsedData["results"][0]["place_id"])
