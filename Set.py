'''
Types of Data Structure in Python:
List , Dictionaries , Tuples , Set
We do use second braket or set function in Set.
'''

num1={1,2,3,4,5}
num2={6,7,8,9,6}
num3=set([7,8,9])
print(num1)
print(num2)
print(num3)

num3.add(6)
print(num3)

num3.remove(9)
print(num3)

print(3 in num3) # It'll check whether 3 exist in num3 set?
print(7 in num3)

print(1 not in num3)

num4={1,2,3,4,5}
num5={4,5,6,7,8}
print(num4 | num5) # | defines union in set
print(num4 & num5) # & defines intersection in set
print(num4 - num5) # - defines difference in set