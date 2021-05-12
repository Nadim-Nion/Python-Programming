'''
In .py file , here we want to read Student.txt file.
But we have to open this file before.
That's we will use open("Name of the file","File's mode").
open() will always return a file and we have to srore this file into a variable
'''


file_open=open("Student.txt","r")

print(file_open.readable())

text = file_open.read()
''' read() will read the file which is belonged to file_open 
and it will store the file into text variable. '''

print(text)

size = len(text)
print(size)


file_open.close()