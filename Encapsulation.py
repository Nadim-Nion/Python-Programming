'''
Encapsulation is a process where we can hide data
Using OOP in Python, we can restrict access to methods and variables.
This prevents data from direct modification which is called encapsulation.
In Python, we denote private attributes using underscore as the prefix
i.e single _ or double __.

self represents the instance of the class.
By using the “self” keyword we can access the attributes and methods of the class in python.
'''

class Person:
    def __init__(self,name,age):
        self.name=name
        self.__age=age

    def display(self):
        print(self.name)
        print(self.__age)


obj=Person("Nion",23)

#accessing using class method
obj.display()

#accessing directly from outside
print("Trying to access variable from outside the class")
print(obj.name)
print(obj.__age)