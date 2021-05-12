class Student:
    Student_ID=""
    CGPA=""

Nion=Student() # Here , Nion is an object of Student Class
# by this method , we can declare object.

print(isinstance(Nion,Student))
#isinstance() checks whether the object_name is the object of that particular class.

Nion.Student_ID=181151746
Nion.CGPA=3.70

print(f"Student ID= {Nion.Student_ID} , CGPA={Nion.CGPA}")
#We can only print the value into the second braket.


Urmi=Student()
Urmi.Student_ID=1611
Urmi.CGPA=3.55

print(f"Student ID= {Urmi.Student_ID} , CGPA={Urmi.CGPA}")
