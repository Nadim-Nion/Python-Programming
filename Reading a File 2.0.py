file_open=open("Student.txt","r")

text=file_open.readlines()
# by using readlines(), we can make a list of Student.txt file's item.



print(text)

file_open.close()

file=open("Student.txt","r")
for line in file:
    print(line)

file.close()

