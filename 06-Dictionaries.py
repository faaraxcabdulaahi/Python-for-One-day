# A Dictionary is a collection which is un-orderded, changeable and indexed. No duplicate numbers. 

'''Dictionary is similar to object literal in javascript. And hash in ruby '''

#1) create a dictionary

person = {
    
    'first_name':'faarax',
    'last_name':'cabdulaahi',
    'age' : 77
    
}
print(person, type(person))

#2) Using a constructor
person2= dict(
    
    first_name='faarax',
    last_name='Cali'
)
print(person2)

#3) Get a value
print(person['first_name']) # Here we use brackets in dictionary

'''There is another way and it is using the get method'''

print(person.get('last_name')) # When you type the get method you have to pass it last_name as parameter. 

#3) Add key value
person['phone']='888-444-444'
print(person)

#4) Get dictionary keys
print(person.keys())

#5) Get the items

print(person.items())

#6) Copy a dictionary
person3 = person.copy()
person3['city']='Galkacyo'
print(person3)

#7) Remove an item
del(person['age'])
print(person)

'''Another way is using pop'''
person.pop('phone')

#8) Clear 
person.clear()
print(person)

#9) Get length
print(len(person2)) 

#10) List of dict
people = [
    
    { 'name':'Faarax',
      'age': 90
     
            },
    {
        'name':'Cismaan',
        'age':89
            }
    
]

print(
    people
)
#11) Accessing a dict


print(people[1]) # It will print the first dictionary

print(people[1]['name']) # It will print dictionary one it's name key. 