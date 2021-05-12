'''
xxargs is used to explain and print  argument with key.
i.e it will print the value with its key.
Note: xxargs works like Dictionaries (Key Based Value)
'''

def students(**details): # Syntax: **text
    print(details)
    print(details["ID"])

students(Name="Nion",ID="181-15-1746")

'''
Here, Name is key 
Nion is the value of the key.

'''