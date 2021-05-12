'''A constructor is a special kind of method
which is used for initializing the instance variables during object creation.
In constructor,we don't call the constructor related _init_() function / method
'''

class Student:
    Student_ID =""
    CGPA =""

    def __init__(self,Student_ID,CGPA): # This is constructor
        self.Student_ID=Student_ID
        self.CGPA=CGPA

    def display(self):   #Here, self is a by default parameter.
        print(f"Student ID = {self.Student_ID} , CGPA = {self.CGPA}")


Nion = Student(181151746,3.70)
Nion.display()

Urmi = Student(1611,3.44)
Urmi.display()