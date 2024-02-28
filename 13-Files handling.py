# Python has functions for creating, reading, updating and deleting files.

#Open a file
myFile = open('myfile.txt', 'w')

#Get some info
print('Name: ', myFile.name) # name dot is property
print('Is Closed: ', myFile.closed)
print('Opening Mode: ', myFile.mode)

# Write to file 
myFile.write('I love Python')
myFile.write('and Flutter')
myFile.close()

# Append (means adding) to file

myFile = open('myfile.txt','a')
myFile.write(' I also like java')
myFile.close()

# Read from file

'''This time we will use r+ as our mode'''
myFile = open('myfile.txt', 'r+')
text = myFile.read(100)
print(text)