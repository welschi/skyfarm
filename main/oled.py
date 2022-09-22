import datetime
currentDateAndTime = datetime.datetime.now()
i = currentDateAndTime.strftime("%H:%M:%S")
print(i)