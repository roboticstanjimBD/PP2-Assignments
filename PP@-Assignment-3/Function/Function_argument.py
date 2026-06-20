"""Arguments
Information can be passed into functions as arguments.

Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:"""


#A function with one argument:

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")


"""Parameters vs Arguments
The terms parameter and argument can be used for the same thing: information that are passed into a function.

From a function's perspective:

A parameter is the variable listed inside the parentheses in the function definition.

An argument is the actual value that is sent to the function when it is called."""



def my_function(name): # name is a parameter
  print("Hello", name)

my_function("Emil") # "Emil" is an argument



"""Number of Arguments
By default, a function must be called with the correct number of arguments.

If your function expects 2 arguments, you must call it with exactly 2 arguments."""


#This function expects 2 arguments, and gets 2 arguments::

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")




"""Default Parameter Values
You can assign default values to parameters. If the function is called without an argument, it uses the default value:"""


def my_function(name = "friend"):
  print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")


# Default value for country parameter:

def my_function(country = "Norway"):
  print("I am from", country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


"""Keyword Arguments
You can send arguments with the key = value syntax."""

def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy")


"""Positional Arguments
When you call a function with arguments without using keywords, they are called positional arguments.

Positional arguments must be in the correct order:"""

#Switching the order changes the result:

def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("Buddy", "dog")


"""Mixing Positional and Keyword Arguments
You can mix positional and keyword arguments in a function call.

However, positional arguments must come before keyword arguments:"""



#You can mix positional and keyword arguments in a function call.

#However, positional arguments must come before keyword arguments:

#Example

def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5)





