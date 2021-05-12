num=[1,2,3,4,5]

result=list(map(lambda x: x*x ,num))

print(result)

#List Comprehensive

numbers=[1,2,3,4,5]

result2=[x*x for x in numbers]
# Syntax=[expression for item in list] .Here item is a variable and it is a item of list.
# Here x*x is the expected output that we are seen in screen.

print(result2)


#List comprehension in Filter()

numbers2=[1,2,3,4,5]

result3=[x for x in numbers if x%2==0 ]

print(result3)