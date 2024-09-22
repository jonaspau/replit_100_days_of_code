import datetime


def getEvent():
    n = input("Enter a name for yout event: ")
    y = int(input("Enter the year: "))
    m = int(input("Enter the month: "))
    d = int(input("Enter the day: "))
    return (n, y, m, d)


today = datetime.date.today()

name, year, month, day = getEvent()

eventDate = datetime.date(year, month, day)
delta = eventDate - today
delta = delta.days

print(eventDate)
print(delta)

if eventDate == today:
    print(f"{name} is happening today!")
elif eventDate > today:
    print(f"{name} is happening in {delta} days")
else:
    print(f"{name} has passed {abs(delta)} days ago")
