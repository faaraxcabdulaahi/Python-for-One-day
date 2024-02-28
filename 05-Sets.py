# A set is a collection which is un-ordered and un-indexed. No duplicate members.  

'''No duplicate memberes means that if you use the add method to add an item which was already in the set, probably it will not add'''

'''A set is created with curly braces'''

'''Set is used when you don't have a duplicate members'''

#1) Creating a set
fruits_set ={'Apples','Oranges','Mango'}

#2) Check if it is in set
print('Apples' in fruits_set)

#3) Add to set (Use add method)

fruits_set.add('Grape')
print(fruits_set)

#4) Removing from set (Use remove method)
fruits_set.remove('Grape')
print(fruits_set)

#5) Clear the set entirely

fruits_set.clear()
print(fruits_set)

'''
Here what happens is it cleared the item that was in the fruit_set data type.

Unlike delet, The entire set + the item will be deleted.

Clear you still have the fruit set but there is nothing in it. 

So there is difference btwn Clear and Del.
 
'''

#6) Deleting a set
del fruits_set
print(fruits_set)
'''Deleting is same as never defining it'''


