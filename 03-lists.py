# A list is a collection which is ordered and changeable. ALlows duplicate members.
'''A list is similar to array'''

# create a list (is the common way to create a list)
numbers = [1,2,3,4,5]

fruits = ['Apples','Oranges','Grapes','Pears']

# Use a constructor
numbers2 = list((1,2,3,4,5))

print(numbers,numbers2)

'''SOME OF THE POPULAR METHODS'''
    #1= Get a value
print(fruits[1])

    #2= Get a length of a value
print(len(fruits))

    #3= Append (Add to at the end of the list)
fruits.append('Mango')
print(fruits)

    #4= Remove from list
fruits.remove('Grapes')
print(fruits)

    #5= Insert into position
fruits.insert(2, 'strawberries') 
''' (2) is the position we want to insert, and the (strawberries) is the item we want to insert'''

    #6= Remove from a certain position with POP
fruits.pop(2) # The 2 defines position two of the item. 
print(fruits)

    #7= Reverse lists
fruits.reverse()
print(fruits)

    #8= Sort the list alphabetically
fruits.sort()
print(fruits)

    #9= Reverse sort
fruits.sort(reverse=True) # Here when you type sort method then you pass it (TRUE REVERSE BOOLEAN)

    #10= Change  a value
fruits[0] = 'Blueberries'
print(fruits)