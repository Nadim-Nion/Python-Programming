def add(a,b):
    sum=a+b
    return sum   #the value will return to whom where it is called from.

result=add(79,32)
'''After returning the output from the add(), we have to store this value into a variable
'''

print("The output is =",result)

def large (x,y):
    if x>y:
        return x
    else:
        return y

maximum=large
print(maximum(10,20))