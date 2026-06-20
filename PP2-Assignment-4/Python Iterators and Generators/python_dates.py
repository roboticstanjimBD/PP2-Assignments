"""Python Dates
A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects."""


import datetime

x = datetime.datetime.now()
print(x)


"""Date Output
When we execute the code from the example above the result will be:

2026-06-20 13:49:03.060842
The date contains year, month, day, hour, minute, second, and microsecond.

The datetime module has many methods to return information about the date object."""


import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))


"""Creating Date Objects
To create a date, we can use the datetime() class (constructor) of the datetime module.

The datetime() class requires three parameters to create a date: year, month, day."""


import datetime

x = datetime.datetime(2023, 5, 17)

print(x)


"""The strftime() Method
The datetime object has a method for formatting date objects into readable strings.

The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:"""

import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%j"))



