import sqlite3
with sqlite3.connect("new.db") as connection:
	c = connection.cursor()

try:
	c.execute("INSERT INTO populations VALUES('New York City', 'NY',8200000)")
	c.execute("INSERT INTO populations VALUES('San Francisco', 'CA', 80000000)")

	conn.commit()

except sqlite3.OperationalError:
	print "Oops! Someting went wrong. Try again..."
	
connection.close()