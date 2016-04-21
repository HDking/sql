#prompt the user whether he or she would like to perform an aggregation (AVG, MAX, MIN, or SUM) or exit the program altoghether
import sqlite3
with sqlite3.connect('newnum.db') as connection:
	c = connection.cursor()

	sql = {'average': "SELECT avg(num) FROM numbers",
			'maximum': "SELECT max(num) FROM numbers",
			'minimum': "SELECT min(num) FROM numbers",
			'sum': "SELECT sum(num) FROM numbers"}

	choice = True
	while choice:
		choice = input("""Please choose one of the following options:
			1. AVG
			2. MAX
			3. MIN
			4. SUM
			0. Quit program
			""")
		try:
			int(choice)
		except:
			print "Please enter a number"
			continue

		if int(choice) > 4 or int(choice) < 0:
			choice = 1
			print "Your number is none of the options"
			print "=================================="
			continue
		elif int(choice) == 0:
			print "Exit"
			break
		else:
			if choice == 1:
				c.execute(sql['average'])
				answer = c.fetchall()
			elif choice ==2:
				c.execute(sql['maximum'])
				answer = c.fetchall()
			elif choice==3:
				c.execute(sql['minimum'])
				answer= c.fetchall()
			elif choice ==4:
				c.execute(sql['sum'])
				answer= c.fetchall()
			print answer[0][0]

