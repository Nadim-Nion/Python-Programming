#sub(pattern,replace,string)
#sub() also returns an object/string

import re
pattern=r"colour"
text="Red is my favourite colour.I love Blue colour as well"

string=re.sub(pattern,"color",text)
print(string)


#count=1 means it will replace only 1st matching item

pattern=r"colour"
text="Red is my favourite colour.I love Blue colour as well"

string=re.sub(pattern,"color",text,count=1)
print(string)