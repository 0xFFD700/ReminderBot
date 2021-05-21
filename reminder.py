from datetime import date
import csv
import os

currentDate = date.today().strftime("%A").lower()

with open('reminder.csv', 'r') as file:
	reader = csv.reader(file, delimiter=';')
	for row in reader:
		if (row[1] == currentDate or row[1] == "everyday") and row[0][1:].isdecimal() and row[0][0] == '+':
			print('signal-cli -u phonenumber send -m "' + row[2] + '" ' + row[0])
			os.system('signal-cli -u +49<TelephonenumberSender> send -m "' + row[2] + '" ' + row[0])
