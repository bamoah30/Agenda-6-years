import datetime

a= datetime.datetime.today()

b= datetime.datetime.now()


print(a)
print(b)


a = datetime.date.today()

b = datetime.date(2020, 5, 27)

c = b - a

print(c)


import calendar

print(calendar.month(1999,5))