from datetime import datetime, date, time, timezone

from_date = date.today()
to_date = date.today()
timenow = datetime.now()
current_time = timenow.strftime("%H:%M:%S")

print(from_date)
print(to_date)
print(current_time)


"""
now = datetime.now()

"""
