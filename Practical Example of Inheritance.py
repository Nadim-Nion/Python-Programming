class Shape:

    def __init__(self,Var1,Var2):
        self.Var1=Var1
        self.Var2=Var2


    def area(self):
        print("I am area method of Shape class")

class Traingle(Shape):

    def area(self):
        area=0.5*self.Var1*self.Var2
        print("Area of Traingle=",area)

class Rectangle(Shape):

    def area(self):
        area=self.Var1*self.Var2
        print("Area of Rectangle=",area)

T=Traingle(20,30)
T.area()
R=Rectangle(20,30)
R.area()


