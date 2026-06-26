

"""A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.

RegEx can be used to check if a string contains the specified search pattern."""


import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)


Function	#Description
findall 	#Returns a list containing all matches
search	    #Returns a Match object if there is a match anywhere in the string
split	    #Returns a list where the string has been split at each match
sub	        #Replaces one or many matches with a string