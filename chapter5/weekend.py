import datetime
#weekdays tuple
weekDays =("monday","tuesday","wednesday","thursday","friday","saturday","sunday")
now = datetime.date.today()
dayOfWeek = now.weekday()
today = weekDays[dayOfWeek]
daysToWeekend= 6-dayOfWeek
print(f"There are {daysToWeekend-1} days until the weekend")
quotedPrinted = "false"
for left in weekDays[dayOfWeek:daysToWeekend]:
    if today == "sunday" and quotedPrinted =="false":
        print(left, "Oh no,....Monday is coming!")
        quotedPrinted = "true"
        break
    elif (today == "monday" or today == "tuesday" or today == "wednesday") and quotedPrinted =="false":
        print(left, "Welp hello work week the work week")
        quotedPrinted = "true"
        break
    elif today == "thursday" and quotedPrinted =="false":
        print(left, "Almost finished")
        quotedPrinted = "true"
        break
    elif quotedPrinted == "false":
        print(left, "Looks like the weekend is here")
        quotedPrinted = "true"
        break
    else:
        print(left)