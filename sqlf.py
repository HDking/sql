import sqlite3

with sqplite3.connect("new.db") as connection:
	c = connection.cursor()

	c.execute("UPDATE population SET population = 900000 WHERE city='New York City'")

	c.execute("DELETE FROM population WHERE city='Boston'")

	print "\nNEW DATA:\n"

	c.execute("SELECT * FROM population")

	rows = c.fetchall()

	for row in rows:
		print r[0], r[1], r[2]