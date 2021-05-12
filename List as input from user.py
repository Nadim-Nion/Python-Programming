number=input("Enter a text of numbers :")
#10 20 30
list = number.split() # 10 , 20 , 30

# split() is used to isolate all numbers from number variable.

sum=0

for x in list:
    sum=sum+int(x)

print("Sum=",sum)

