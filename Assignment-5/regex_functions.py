## findall - The findall() function returns a list containing all matches.

import re
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

"""The search() Function
The search() function searches the string for a match, and returns a Match object if there is a match.

If there is more than one match, only the first occurrence of the match will be returned:"""

import re
txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)


## Split Function :

# The split() function returns a list where the string has been split at each match:

import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)


## using maxsplit You can control the number of occurrences by specifying the

import re

txt = "The rain in Spain"
x = re.split("\s", txt, 2)
print(x)


## Sub Function ##
# The sub() function replaces the matches with the text of your choice:

import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)