import sqlite3
import re

conn = sqlite3.connect("py4e_db.sqlite")

cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS Counts")

cur.execute("CREATE TABLE Counts (org varchar(128), count integer)")

fhandler = open("../mbox.txt")
orgs = list()
for line in fhandler:
    if not line.startswith("From: "):
        continue
    else:
        orgs += re.findall("@([^ ]+)", line.strip())
        orgs_count = dict()

for org in orgs:
    orgs_count[org] = orgs_count.get(org, 0) + 1
for item in orgs_count:
    cur.execute("INSERT INTO Counts (org, count) VALUES (?, ?)", (item, orgs_count[item]))
conn.commit()

rows = cur.execute("SELECT * FROM Counts ORDER BY count DESC LIMIT 10")
for row in rows:
    print str(row[0]), row[1]

cur.close()
