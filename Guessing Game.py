from random import randint

for x in range(1,6):
  guessVariable=int(input("Enter any number from 1 to 5:"))
  randomVariable=randint(1,5)



  if guessVariable==randomVariable:
     print("Yes,You've won.")
  else:
     print("No,You've lost.")
     print("Random Variable was=",randomVariable)
