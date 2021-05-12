class A:
    def display(self):
        print("I am inside A class")

class B:
    def display(self):
        print("I am inside B class")


class C(A,B):
    #A-> display()
    #B-> display()

    '''def display(self):
        print("I am inside C class")'''

obj=C()
obj.display()