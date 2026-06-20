""" A function is a block of code which only runs when it is called.

A function can return data as a result.

A function helps avoiding code repetition.
"""

# In Python, a function is defined using the def keyword, followed by a function name and parentheses:

def my_function():
  print("Hello from a function")

  # To call a function, write its name followed by parentheses:

def my_function():
  print("Hello from a function")

my_function()



"""Why Use Functions?
Imagine you need to convert temperatures from Fahrenheit to Celsius several times in your program. Without functions, you would have to write the same calculation code repeatedly:"""

 # WITHOUT FUNCTION
temp1 = 77
celsius1 = (temp1 - 32) * 5 / 9
print(celsius1)

temp2 = 95
celsius2 = (temp2 - 32) * 5 / 9
print(celsius2)

temp3 = 50
celsius3 = (temp3 - 32) * 5 / 9
print(celsius3)


# WITH FUNCTION

def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))

"""Return Values
Functions can send data back to the code that called them using the return statement.

When a function reaches a return statement, it stops executing and sends the result back:
"""


def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message)
