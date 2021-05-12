'''' Continue keyword : when true/match incident is happened while using continue keyword ,

it will again send the cursor to the loop

'''

i=1

while i<=100 :
    if i==20 :
        continue
    print(i)
    i=i+1
    '''+
    if i==20 :
        continue'''

print("End")