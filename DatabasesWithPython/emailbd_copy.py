import sqlite3
import re

conn = sqlite3.connect("py4e_db.sqlite")

cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS Counts")

cur.execute("CREATE TABLE Counts (email varchar(128), count integer)")

fhandler = open("../mbox.txt")
for line in fhandler:
    if not line.startswith("From: "):
        continue
    else:
        pieces = line.split()
        email = pieces[1]

        cur.execute("SELECT COUNT(*) FROM Counts WHERE EMAIL = ?", (email, ))
        rows = cur.fetchone()
        if rows[0] == 0:
            cur.execute("INSERT INTO Counts (email, count) VALUES (?, 1)", (email, ))
        else:
            cur.execute("UPDATE Counts SET count = count + 1 WHERE email = ?", (email, ))
conn.commit()

rows = cur.execute("SELECT * FROM Counts ORDER BY count DESC LIMIT 10")
for row in rows:
    print str(row[0]), row[1]

cur.close()
