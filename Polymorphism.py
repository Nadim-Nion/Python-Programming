'''
Polymorphism : The word polymorphism means having many forms.
In programming, polymorphism means same function name (but different signatures)
being uses for different types.
'''



#Built in polymorphic function

print(len("Nadim Mahmud Nion"))
print(len([10,20,30]))


#User defined polymorphic function

def add(x,y,z=0):
    return x+y+z

print(add(10,20))
print(add(10,20,30))