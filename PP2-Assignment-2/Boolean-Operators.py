#1. The and Operator
#Returns True only if both conditions are true. If even one condition is false, it returns False.

x = 7
y = 12

# Both conditions are True (7 > 5 and 12 < 20)
print(x > 5 and y < 20)  # Output: True

# One condition is False (12 is not less than 10)
print(x > 5 and y < 10)  # Output: False



#2. The or Operator
#Returns True if at least one of the conditions is true. It only returns False if both conditions are false.


x = 7
y = 12

# One condition is True (7 > 5), so the whole thing is True
print(x > 5 or y < 10)  # Output: True

# Both conditions are False (7 is not greater than 10, and 12 is not less than 5)
print(x > 10 or y < 5)  # Output: False


#3. The not Operator
#Used to reverse the Boolean value. It turns True into False, and False into True.


is_raining = True

# Reverses True to False
print(not is_raining)  # Output: False

x = 10
y = 20
# x > y is False, so "not False" becomes True
print(not x > y)       # Output: True



'''Quick Summary Truth Table
Operator	Expression	Result	Description
and	True and False	False	Requires all to be True
or	True or False	True	Requires any to be True
not	not True	False	Flips the result'''