# Debugging: Debugging is the process when we are able to find a bug or error from the code.

def add(*numbers):
    sum=0

    for num in numbers:
        sum=sum+num

    return sum

print(add(10,20))