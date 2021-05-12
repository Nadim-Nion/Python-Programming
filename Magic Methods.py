class Bike:
    def __init__(self,name,color):
        self.name=name
        self.color=color


    def __str__(self): #This is Magic Method
        return (f"Name={self.name},Color={self.color}")


    def __eq__(self, other):
        return self.name==other.name and self.color==other.color



    def display(self):
        print(f"Name={self.name},Color={self.color}")

bike1=Bike("Yamaha R15","Red")
bike2=Bike("Yamaha R15","Red")

print(str(bike1))
print(str(bike2)) # __str__ () will print the value of the object

print(bike1==bike2)
