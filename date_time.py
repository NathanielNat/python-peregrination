import datetime

# print(datetime.datetime.now())

# dt = datetime.datetime(2015, 10, 21, 16, 29, 0)
# print(dt.year, dt.month, dt.day)


# delta = datetime.timedelta(days = 11, hours = 10, minutes= 9, seconds=7)

# print(delta.days,delta.seconds,delta.microseconds)
# print(delta.total_seconds())
# print(str(delta))


print(datetime.datetime.strptime('October 21, 2015', '%B %d, %Y'))
print(datetime.datetime.strptime('2015/10/21 16:29:00', '%Y/%m/%d %H:%M:%S'))
