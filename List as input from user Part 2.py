numOfLetter=0
numOfDigit=0
numOfWord=0

text=input("Enter any text : ") # My name is nion72

for x in text:

    x = x.lower()
    # lower() is used to convert all capital letter into lower letter.
    if x>='a' and x<='z':
        numOfLetter = numOfLetter+1

    elif x>='0' and x<='9':
        numOfDigit = numOfDigit+1

    elif x==' ':
        numOfWord=numOfWord+1

print("Number of Letters",numOfLetter)
print("Number of Digits",numOfDigit)
print("Number of words",numOfWord+1)
