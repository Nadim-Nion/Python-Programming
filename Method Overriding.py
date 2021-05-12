'''Method overriding, in object-oriented programming,
 is a language feature that allows a subclass or child class
 to provide a specific implementation of a method
 that is already provided by one of its superclasses or parent classes. '''

class Phone:
    def __init__(self):
        print("I am in Phone class")


class Samsung(Phone):

    def __init__(self):
        super().__init__()    # To call properties of super class
        print("I am in Samsung class")

S=Samsung()