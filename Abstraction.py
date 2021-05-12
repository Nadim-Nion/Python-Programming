'''Abstract Method:When a method hasn't any body ,
then the method is called abstract method

Abstract Class:When a class contains an abstract method ,
then the class is called abstract class
We can't create and declare a object for any abstract class

Abstraction: Abstraction is used to hide the internal functionality of the function
from the users. The users only interact with the basic implementation
of the function, but inner working is hidden.
User is familiar with that "what function does" but they don't know "how it does."
'''

from abc import ABC,abstractclassmethod
class Shape(ABC): #ABC stands for Abstraction Base Class
    def __init__(self,dim1,dim2):
        self.dim1=dim1
        self.dim2=dim2

    @abstractclassmethod
    def area(self):
        pass


class Triangle(Shape):
    #_init()
    # area()

    def area(self):
        area=0.5*self.dim1*self.dim2
        print("Area of Triangle=",area)


class Rectangle(Shape):
    #_init()
    # area()

    def area(self):
        area=self.dim1*self.dim2
        print("Area of Rectangle=",area)

#S=Shape(10,20)
#S.area()
T=Triangle(10,20)
T.area()
R=Rectangle(10,20)
R.area()