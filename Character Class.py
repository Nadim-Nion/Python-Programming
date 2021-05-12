#A "character class", or a "character set", is a set of characters put in square brackets.
# [abc] - Matches a or b or c.
import re
pattern=r"[aeiou]"
# at least one character of this set should match with the string in the beginning

if re.match(pattern,"nyaegvavag"):
    print("Match")
else:
    print("Not Match")


# [a-zA-Z0-9] - Matches any letter from (a to z) or (A to Z) or (0 to 9).

import re
pattern=r"[A-Z]"
# at least one character of this set should match with the string in the beginning

if re.match(pattern,"yevavaZ"):
    print("Match")
else:
    print("Not Match")


import re
pattern=r"[0-9]"
# at least one character of this set should match with the string in the beginning

if re.match(pattern,"6yevavaZ"):
    print("Match")
else:
    print("Not Match")



import re
pattern=r"[A-Z][a-z[0-9]"
# at least one character of this set should match with the string in the beginning

if re.match(pattern,"Gv6yevavaZ"):
    print("Match")
else:
    print("Not Match")