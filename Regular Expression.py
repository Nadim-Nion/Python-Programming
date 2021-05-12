import re
pattern=r"Red"  # r" "= row string

#match() matches pattern with the beginning of the string
if re.match(pattern,"Red is a colour.I don't like this colour"):
    print("Match")

else:
    print("Not Match")





pattern=r"colour"

#search() tries to match the pattern with the whole string
if re.search(pattern,"Red is a colour"):
    print("Match")
else:
    print("Not Match")




pattern=r"color"

'''findall() matches the pattern with the whole string. 
If numerous string match with the pattern,then this fuction will return a list
'''

print(re.findall(pattern,"Green is my favourite color. I love this color"))


