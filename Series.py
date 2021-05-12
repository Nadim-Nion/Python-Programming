#1+2+3+....+n

n=int(input("Enter Any Number="))

sum = 0

for x in range(1,n+1,1):
    sum = sum + x
print("Summation=",sum)


#2+4+6+....+m

m=int(input("Enter Any Number="))

sum2 = 0

for y in range(2,m+1,2):
    sum2 = sum2 + y
print("Summation=",sum2)