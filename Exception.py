# Exception is a runtime error / incorrect input / incorrect code

try:
 list=[20,0,30]

 result = list[0] / list[3]

 print(result)
 print("Done")


except ZeroDivisionError :
    print("Diving by zero is not possible")


finally:
   print("Successful")