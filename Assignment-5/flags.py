## re.ASCII	re.A	Returns only ASCII matches:

import re
txt = " its haland vs dictator"
x= re.findall("\w",txt,re.A)
print(x)


# re.DEBUG		Returns debug information
print(re.findall("dictator",txt,re.DEBUG))

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
## re.DOTALL	re.S	Makes the . character match all characters (including newline character)


import re
txt= """HI
 my 
 name
 is 
 TANJIM"""

x= re.findall("me.is", txt, re.DOTALL)
print(x)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

## re.IGNORECASE	re.I	Case-insensitive matching:

import re

txt = "The rain in Spain"

#Use a case-insensitive search when finding a match for Spain in the text:
print(re.findall("spain", txt, re.IGNORECASE))


#Same result using the shorthand re.I flag:
print(re.findall("spain", txt, re.I))




""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# re.MULTILINE	re.M	Returns matches at the start/end of each line:

import re

txt = """There
aint much
rain in 
Spain"""

print(re.findall("^ain",txt,re.MULTILINE))
print(re.findall("aint$",txt,re.MULTILINE))



""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# re.UNICODE	re.U	
"""Returns Unicode matches.
 This is default from Python 3.
 For Python 2: use this flag to return only Unicode matches"""

import re

txt = "Åland"

#Find all UNICODE matches:
print(re.findall("\w", txt, re.UNICODE))


#Same result using the shorthand re.U flag:
print(re.findall("\w", txt, re.U))




""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# re.VERBOSE	re.X
"""Allows whitespaces
 and comments inside patterns.
   Makes the pattern more readable"""

import re

text = "The rain in Spain falls mainly on the plain"

#Find and return words that contains the phrase "ain":

pattern = """
[A-Za-z]* #starts with any letter
ain+      #contains 'ain'
[a-z]*    #followed by any small letter
"""

print(re.findall(pattern, text, re.VERBOSE))

#The example would return nothing without the re.VERBOSE flag
print(re.findall(pattern, text))


#Same result with the shorthand re.X flag:
print(re.findall(pattern, text, re.X))

