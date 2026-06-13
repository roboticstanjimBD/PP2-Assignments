#If you have one statement for if and one for else, you can put them on the same line using a conditional expression:


a = 2
b = 330
print("A") if a > b else print("B")

#Multiple Conditions in one Line

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#example

#Finding the maximum of two numbers:

x = 15
y = 20
max_value = x if x > y else y
print("Maximum value:", max_value)