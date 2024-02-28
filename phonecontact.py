import sqlite3

conn = sqlite3.connect('contacts.db')

c = conn.cursor()

#c.execute("""CREATE TABLE contacts (
#          name text,
#          id integer,
#          phone integer,
#         email text
#)""")

#c.execute("INSERT INTO contacts VALUES ('alex',001,1234567890,'alex@gmail.com')")
#c.execute("INSERT INTO contacts VALUES ('bob',001,9876543210,'bob@gmail.com')")
#c.execute("INSERT INTO contacts VALUES ('clara',001,1357924680,'clara@gmail.com')")
#c.execute("INSERT INTO contacts VALUES ('daniel',001,2468013579,'daniel@gmail.com')")
#c.execute("INSERT INTO contacts VALUES ('emily',001,1029384756,'clara@gmail.com')")

conn.commit()

c.execute("SELECT * FROM contacts WHERE id=001")

print(c.fetchall())

conn.commit()

conn.close()