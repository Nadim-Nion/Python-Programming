# more method with seatch(). search() will return an object

import re

pattern = r"colour"
text = "Blue is my favourite colour"

match = re.search(pattern, text)
if match:
    print(match.start())
    print(match.end())
    print(match.span())

'''
start() - Returns the starting index of the match.
end() - Returns the index where the match ends.
span() - Return a tuple containing the (start, end) positions of the match.
 
 '''