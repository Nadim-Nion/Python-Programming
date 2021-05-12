#raise keyword

def voter(age):
    if age < 18:
      raise ValueError("Invalid Voter") # ValueError is an exception
    return "You are allowed to vote"
try:
  print(voter(18))
  print(voter(15))

except ValueError as v: # by using as keyword , we can rename the exception 
    print(v)
