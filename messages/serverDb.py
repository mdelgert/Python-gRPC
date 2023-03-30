#https://docs.python.org/3/library/sqlite3.html
#https://www.sqlitetutorial.net/sqlite-python/
#https://www.digitalocean.com/community/tutorials/how-to-use-the-sqlite3-module-in-python-3
#https://docs.python.org/3/tutorial/modules.html
#https://www.w3schools.com/python/python_modules.asp

import sqlite3

def deleteMessages():                                        
    conn = sqlite3.connect("messages.db")
    cursor = conn.cursor()
    sql = "DELETE FROM messages;"
    cursor.execute(sql)
    conn.commit()
    conn.close()

def createTable():
    conn = sqlite3.connect("messages.db")
    cursor = conn.cursor()
    sql = "CREATE TABLE messages (Id INTEGER PRIMARY KEY, message TEXT, messageType TEXT);"
    cursor.execute(sql)
    conn.commit()
    conn.close()

def createMessage(message):
    print("Message=" + message)
    conn = sqlite3.connect("messages.db")
    print(conn.total_changes)
    cursor = conn.cursor()
    sql = "INSERT INTO messages (message, messageType) VALUES ('" + message + "', 'type2')"
    cursor.execute(sql)
    rows = cursor.execute("SELECT * FROM messages").fetchall()
    print(rows)
    conn.commit()
    conn.close()