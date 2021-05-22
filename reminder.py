from datetime import date
import csv
import os

currentDate = date.today().strftime("%A").lower()

with open('reminder.csv', 'r') as file:
	reader = csv.reader(file, delimiter=';')
	for row in reader:
		if (row[2] == currentDate or row[2] == "everyday"):
			if(row[1] == "person"):
				print('signal-cli -u $USERNAME send -m "' + row[3] + '" ' + row[0])
				os.system('signal-cli -u $USERNAME send -m "' + row[3] + '" ' + row[0])
			else:
				print('signal-cli -u $USERNAME send -m "' + row[3] + '" -g ' + row[0])
				os.system('signal-cli -u $USERNAME send -m "' + row[3] + '" -g ' + row[0])
