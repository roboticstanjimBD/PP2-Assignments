# use of []:
import re
txt = "The rain in Spain"
#Find all lower case characters alphabetically between "a" and "m"
x= re.findall("[a-p]",txt)
print(x)

# "\" use :

import re
txt = "That will be 59.00 dollars"
#find the digits#

x=re.findall("\d\.\d",txt)
print(x)


# "."  any charachter except newline chr

import re
txt= "hello planet"
#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":
x= re.findall("he..o", txt)
print(x)


# "^" anything starts with a targeted :

import re

txt = "hello planet"

#Check if the string starts with 'hello':

x = re.findall("^hello", txt)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")


# ends with something "$":

import re

txt = "hello planet"

#Check if the string ends with 'planet':

x = re.findall("planet$", txt)
if x:
  print("Yes, the string ends with 'planet'")
else:
  print("No match")



## find >=0 occurances use "*":

import re

txt = "hello planet"

#Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":

x = re.findall("he.*o", txt)

print(x)



## Find >= 1 occurances:

import re

txt = "hello planet"

#Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o":

x = re.findall("he.+o", txt)

print(x)



## Zero or One occurances:

import re

txt = "hello planet"

#Search for a sequence that starts with "he", followed by 0 or 1  (any) character, and an "o":

x = re.findall("he.?o", txt)

print(x)

#This time we got no match, because there were not zero, not one, but two characters between "he" and the "o"

