import sqlite3

conn = sqlite3.connect('emails.db')
cursor = conn.cursor()
cursor.execute("PRAGMA table_info(email);")
columns = cursor.fetchall()

for col in columns:
    print(col)

conn.close()
