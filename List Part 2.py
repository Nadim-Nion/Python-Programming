subjects=["Bangla","English","Math","Physics","Chemistry","Biology"]
print(len(subjects))

subjects.append("ICT")
subjects.append(23)
# Append function is used to add items into the List

print(subjects)

subjects.insert(2,"Practical")
print(subjects)

subjects.remove(23)
print(subjects)

subject=[20,50,10,40,33]
subject.sort() # This function is used to sort at ascending order
print(subject)

subject.reverse() # This function is used to sort at descending order
print(subject)

subject.pop() # This funtion is used to eliminate the last item of the list
print(subject)

subject.clear() # This function will clear all list's item.
print(subject)

subjects2= subjects.copy()
print(subjects2)

pos=subjects2.index('Math')
''' This function is used to find the index number of any item. 
This function will also return a value and we have to store this value in any variable.
'''
print(pos)

numbers=[4,5,6,7,5,6,7,8,5,5]
compute=numbers.count(5)
''' This function is used to count the number of desired item into the list.
This function also return a int value and we have to store this value into any variable
'''
print(compute)