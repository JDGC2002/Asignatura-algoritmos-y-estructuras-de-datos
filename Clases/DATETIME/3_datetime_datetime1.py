from datetime import datetime
from datetime import date
from datetime import time

#from datetime import datetime, date, time

my_datetime = datetime(1999, 12, 12)
print(my_datetime)
  
my_datetime = datetime(1999, 12, 12, 12, 12, 12, 342380)
print(my_datetime)

my_datetime = datetime.now()
print(my_datetime)

# Algunos atributos:
print("year =", my_datetime.year)
print("month =", my_datetime.month)
print("hour =", my_datetime.hour)
print("minute =", my_datetime.minute)

# ¿Qué es el timestamp?
print("timestamp =", my_datetime.timestamp())

print(datetime.fromtimestamp(1, tz=None))
print(datetime.fromtimestamp(100, tz=None))
print(datetime.fromtimestamp(1000000000, tz=None))
# ¿entiende?

# función combine:
my_date = date(1996, 12, 11)
my_time = time(8, 55, 0)
new_datetime = datetime.combine(my_date, my_time)
print(new_datetime)

