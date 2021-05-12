books=[]

books.append("Learn C") # append() is used to push value into the stack
books.append("Learn C++")
books.append("Learn Java")

print(books)

books.pop()
print(books)
print("The top most book is : ",books[-1])
# -1 index always show the last item

books.pop()
print(books)
print("The top most book is : ",books[-1])

books.pop()
if not books:
    print("Not books left")