''' Lambda Function: A function without any name
Not powerful as Named Function
It can work single expression or single line of code '''

def result(a,b):
     return a*a + 2*a*b + b*b

print(result(2,3))

# Syntax of Lambda function= lambda parameter : expression
result=(lambda a,b : a*a + 2*a*b + b*b)(2,3)
print(result)

def cube(x):
     return x*x*x
print(cube(2))


output=(lambda x : x*x*x)(2)
print(output)