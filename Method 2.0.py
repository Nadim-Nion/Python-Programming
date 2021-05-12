class Student:
    Student_ID =""
    CGPA =""

    def set_value(self,Student_ID,CGPA):
        self.Student_ID=Student_ID
        self.CGPA=CGPA

    def display(self):   #Here, self is a by default parameter.
        print(f"Student ID = {self.Student_ID} , CGPA = {self.CGPA}")


Nion = Student()
Nion.set_value(181151746,3.70)
Nion.display()

Urmi = Student()
Urmi.set_value(1611,3.44)
Urmi.display()