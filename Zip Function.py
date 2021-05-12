roll=[101,102,103,104,105]
name=["Nadim","Nion","Nishad","Tazin","Tamanna"]

# Zip() always return a list value / iterative object.

result=list(zip(roll,name))

print(result)

result2=list(zip(roll,name,"ABCDE"))

print(result2)