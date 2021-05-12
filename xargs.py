'''
xargs is used to print multiple numbers of arguments for the same number of parameter.
if we change the numbers of argument , the function still can print the output.
Note: xargs works like Tuples.
'''

def add(*details):# syntax: def function_name(*text)
    print(details)
    print(details[1])

add(101,"Physics")
add(102,"Chemistry","Ch 1st paper")

def summation(*numbers):
    sum=0
    for x in numbers:
        sum= sum+x
    print("Summation is =",sum)

summation(10,20)
summation(10,20,50)
summation(10,20,50,70)

