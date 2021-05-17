# ReminderBot
Reminder Bot for Signal and Discord.

## Setup Discord
Install Discord.py `python3 -m pip install -U discord.py`.

## Setup Signal
Run signal-cli config in the Terminal (credit https://github.com/AsamK/signal-cli)
```
./signal-cli -u +49<TelephonenumberSender> register
./signal-cli -u +49<TelephonenumberSender> verify <SecurityCode>
./signal-cli -u +49<TelephonenumberSender> send -m “Hello World” +49<TelephonenumberReciever>
```

## Customize Script
Change the ```+49<TelephonenumberSender>``` in ReminderBot.py to your phonenumber.

## Set Reminders
Make a CVS with the format <service>,<reciever>,<day>,<message> and name it Reminder.csv.
- service: discord or signal
- receiver: phonenumber or discord-token
- day: monday, tuesday, wednesday, thursday, friday, saturday, sunday or everyday
```
signal;+4912345678910;monday;Hier könnte ihre Werbung stehen!
discord;<discord token>;everyday;Today something is happening!
```
  
## Start script
Make a cronjob that runs ReminderBot.py once a day at whatever time you want to send the Reminder.
