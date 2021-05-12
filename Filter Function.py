'''
# The filter() method filters the given sequence with the help of a function
that tests each element in the sequence to be true or not.
This function returns iterative object (List) like map().
'''

numbers=[1,2,3,4,5]

result=list(filter(lambda x: x%2==0 , numbers))

print(result)