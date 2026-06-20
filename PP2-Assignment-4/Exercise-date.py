
1. Write a Python program to subtract five days from current date.

from datetime import datetime, timedelta
current_date= date.today()
before_five_days= current_date - timedelta(days=5)
print("5 days ago: ", before_five_days)



2. Write a Python program to print yesterday, today, tomorrow.

from datetime import date, timedelta


today = date.today()

yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:    ", today)
print("Tomorrow: ", tomorrow)



3. Write a Python program to drop microseconds from datetime.

from datetime import datetime
time = datetime.now()
new_time = time.replace(microsecond=0)
print(new_time)



4. Write a Python program to calculate two date difference in seconds.


from datetime import datetime

date1 = datetime(2026, 6, 20, 14, 30, 0)  # June 20, 2026, 2:30 PM
date2 = datetime(2026, 6, 15, 10, 0, 0)   # June 15, 2026, 10:00 AM


time_difference = date1 - date2

seconds_difference = time_difference.total_seconds()


print(seconds_difference)
