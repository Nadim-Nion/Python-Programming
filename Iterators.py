#An iterator is an object that contains a countable number of values.
'''An iterator is an object which implements the iterator protocol,
which consist of the methods __iter__() and __next__().'''

'''Iterator vs Iterable : Lists, tuples, dictionaries, and sets are all iterable objects. 
They are iterable containers which you can get an iterator from.
All these objects have a iter() method which is used to get an iterator. '''


#Return an iterator from a tuple, and print each value:
fruits=("Mango","Banana","Watermelon")
myit=iter(fruits)
print(next(myit))
print(next(myit))
print(next(myit))


#Strings are also iterable objects, containing a sequence of characters:
fruits=("Mango")
myit=iter(fruits)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
