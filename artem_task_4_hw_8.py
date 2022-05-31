import datetime

now = datetime.datetime.now()

year = (lambda x: list(datetime.datetime.timetuple(now))[0])
month = (lambda x: list(datetime.datetime.timetuple(now))[1])
day = (lambda x: list(datetime.datetime.timetuple(now))[2])

print(year(now))
print(month(now))
print(day(now))


# datetime documentation
https://docs.python.org/3/library/datetime.html