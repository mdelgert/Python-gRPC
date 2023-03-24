#https://docs.python.org/3/library/sqlite3.html
#https://www.sqlitetutorial.net/sqlite-python/
#https://www.digitalocean.com/community/tutorials/how-to-use-the-sqlite3-module-in-python-3

import sqlite3

conn = sqlite3.connect("messages.db")

print(conn.total_changes)

cursor = conn.cursor()

#cursor.execute("CREATE TABLE messages (Id INTEGER PRIMARY KEY, message TEXT, messageType TEXT);")

cursor.execute("INSERT INTO messages (message, messageType) VALUES ('message2', 'type2')")

rows = cursor.execute("SELECT * FROM messages").fetchall()

print(rows)

conn.commit()

conn.close()