class Phone:
    call=""
    message=""

    def call(self):
        print("You can call")

    def message(self):
        print("You can message")

#Here, Phone class is Super class or Base lass or Parent class
#Samsung class is Sub class or Derived class or Child class

class Samsung(Phone):
#All the methods of Phone class has come to the Samsung class by using Inheritance

    def Photo(self):
        print("You can take photo")


#Creating and declaring object

S=Samsung()
S.call()
S.message()
S.Photo()

#We'll check whether Samsung is a sub class of Phone

print(issubclass(Samsung,Phone))