# SignalReminder
Reminder Bot for Signal.

## Setup Signal
Run signal-cli config in the Terminal (credit https://github.com/AsamK/signal-cli)
```
./signal-cli -u +49<TelephonenumberSender> register
./signal-cli -u +49<TelephonenumberSender> verify <SecurityCode>
./signal-cli -u +49<TelephonenumberSender> send -m “Hello World” +49<TelephonenumberReciever>
```

## Customize Script
- Change the ```+49<TelephonenumberSender>``` in ReminderBot.py to your phonenumber.

## Set Reminders
Make a CVS with the format <reciever>,<day>,<message> and name it Reminder.csv.
- receiver: phonenumber
- day: monday, tuesday, wednesday, thursday, friday, saturday, sunday or everyday
```
+4912345678910;monday;Hier könnte ihre Werbung stehen!
12324234183172;everyday;Today something is happening!
```
  
## Start script
Make a cronjob that runs ReminderBot.py once a day at whatever time you want to send the Reminder.
