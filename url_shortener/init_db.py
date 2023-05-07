import sqlite3

connection = sqlite3.connect('links.db')


with open('SQL/schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO links (original, short) VALUES (?, ?)",
            ('www.youtube.com/watch?v=dQw4w9WgXcQ', 'iykyk')
            )

cur.execute("INSERT INTO links (original, short) VALUES (?, ?)",
            ('www.google.com', 'elgoog')
            )

connection.commit()
connection.close()