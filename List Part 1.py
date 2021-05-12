#List is an object of Python where we can store many items.

subject=["C","C++","Java","Python","Android","OS","TOC"]
# We have to use third bracket while adding items into the List.

print(subject)
print(subject[5])
print(subject[3:]) # This will print all items from 3rd item to last item.
print(subject[-1]) # -1 indicates last item and -2 indicate 2nd last item.

print("C" in subject)

'''by using in operator , we can search an item into the list.
If the item is found at List, IDE will return true , otherwise  it will return false.
'''

print("Swift" not in subject)

print(subject * 3) # It will show all the List's item thrice

print(subject + ["Swift" , 23] ) # We have to use third bracket outside the items.

# When we add items into the list , we have to use Add operator