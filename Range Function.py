# Range function is used to print the value of any range

num = list(range(20))

''' range() is used to generate 20 values ( 0 to 19 ) . 
by using list(),we can contain all of these values (it can contain multiple values). 
Though list() returns value , we have to store these values into a variable. '''

print(num)

print(num[17])


digit=list(range(5,15))
'''Here, 5 is starting point and 15 is ending point. 
This range() will print the value from 5 and it will be printing before the ending point
i.e it will print the value till 14
We know that the index of List will start from 0. 
'''
print(digit)

value=list(range(2,105,3))
# here , 2 is starting point , 105 is ending point and 3 is interval
print(value)