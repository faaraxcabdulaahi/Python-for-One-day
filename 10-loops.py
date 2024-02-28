# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set or a string). 

#A= for that loops over a list
    
people = ['cali','jaamac','geele','cismaan']

'''Asimple for loop'''
for person in people:
    print(f'current person: {person}')
    
'''Break a loop'''
for person in people:
    if person == 'cismaan':
        break
    print(f'current person: {person}')
    
'''Continue loop'''
for person in people:
    if person == 'cismaan':
        continue
    print(f'current person: {person}')
#B) Rang looping
for i in range(len(people)):
    print(people[i])
    
#C) Custome range
for i in range (0,11):
    print(f'Number: {i}') 
'''Here what will hapen is that it will print 1 to 10'''

#While loops execute a set of statements as long as a condition is true. 

count = 0
while count <= 10:
    print(f'count:{count}')
    count += 1