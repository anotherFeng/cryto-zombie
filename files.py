# Python has functions for creating, reading, updating, and deleting files.

myFile = open('myFile.txt', 'w')

print('Name: ', myFile.name)
print('Is Closed: ', myFile.closed)
print('Opening Mode: ', myFile.mode)

myFile.write('I love Python')
myFile.close()

myFile = open('myFile.txt', 'a')
myFile.write(' and Javascript')
myFile.close()

myFile = open('myFile.txt', 'r+')
text = myFile.read(10)
print(text)