# SignalReminder
Reminder Bot for Signal.

## Setup Signal
Run signal-cli config in the Terminal (credit https://github.com/AsamK/signal-cli)
```
./signal-cli -u +49<TelephonenumberSender> register
./signal-cli -u +49<TelephonenumberSender> register --captcha <captchacode>
./signal-cli -u +49<TelephonenumberSender> verify <SecurityCode>
./signal-cli -u +49<TelephonenumberSender> send -m “Hello World” +49<TelephonenumberReciever>
```

## Join a group
```
#Join with the invitelink and get the group id as a response
./signal-cli -u +49<TelephonenumberSender> joinGroup --uri <invitelink>
./signal-cli -u +49<TelephonenumberSender> send -g <groupid> -m “Hello World”
```

## Customize Script
- Change the ```+49<TelephonenumberSender>``` in reminder.py to your phonenumber.

## Set Reminders
Make a CVS with the format <reciever>,<group or person>,<day>,<message> and name it Reminder.csv.
- receiver: phonenumber or groupid
- group or person: specifies if you want to message a group or single person
- day: monday, tuesday, wednesday, thursday, friday, saturday, sunday or everyday
```
+4912345678910;person;monday;Hier könnte ihre Werbung stehen!
GTAHYc0dieGruppepb/OjMT7/RRNGNorHyw2hsQ0=;group;everyday;Today something is happening!
```
  
## Start script
Make a cronjob that runs ReminderBot.py once a day at whatever time you want to send the Reminder.
