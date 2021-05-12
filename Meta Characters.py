#.(Dot) = A period. Matches any single character except the newline character.

import re
pattern=r".olour"

if re.match(pattern,"Colour"):
    print("Match")
else:
    print("Not Match")


#^  - A caret. Matches the start of the string.
#$ - Matches the end of string.
import re
pattern=r"^Col...r$" # ^ = Start of String , $ = End of String

if re.match(pattern,"Colour"):
    print("Match")
else:
    print("Not Match")


#* - Checks if the preceding character appears zero or more times starting from that position.

import re
pattern1=r"a*" #Zero or more a may remain
if re.match(pattern1,"hygbg"):
    print("Match")
else:
    print("Not Match")

pattern2=r"(ab)*" #Zero or more ab may remain
if re.match(pattern2,"abababa"):
    print("Match")
else:
    print("Not Match")



#+ - Checks if the preceding character appears one or more times starting from that position.

import re
pattern=r"a+" # one or more a (at least one a) can remain
if re.match(pattern,"bhyyg"):
    print("Match")
else:
    print("Not Match")


''' ? - Checks if the preceding character appears 
 exactly zero or one time starting from that position.'''
import re
pattern=r"ice(-)?cream"
if re.match(pattern,"ice-cream"):
    print("Match")
else:
    print("Not Match")


'''
{x} - Repeat exactly x number of times.
{x,} - Repeat at least x times or more.
{x, y} - Repeat at least x times but no more than y times.

'''

import re
pattern=r"a{1,3}$" # at least 1 times 'a' but not more 'a' than 3 times
# Here, $ = End of symbol

if re.match(pattern,"aaaa"):
    print("Match")
else:
    print("Not Match")