'''
#The map() function applies a given function to each item of an iterable (list, tuple etc.)
and returns a list of the results.
'''


def square(x):
    return x*x

numbers=[1,2,3,4,5]


result=list(map(square,numbers))
print(result)
