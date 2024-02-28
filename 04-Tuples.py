# A Tuple is a collection which is ordered and unchageable. Allows duplicate members.
'''The important thing of the Tuple unchageable'''
'''To create a tuple you have to use the parenthesis'''

# 1)Create a tuple 
fruits1 = ('Apple','Oranges','Grapes')

'''You have to remember that in tuples if you have a single item and you don't but it after it a comma, it will be a string'''

#Single value needs trailing comma

fruits = ('Apple') # It is a string
fruits = ('Apple',) # it is a tuple



# 2) Use a constructor
 
fruits2 = tuple(('Apple','Oranges','Grapes'))
print(fruits2)


    # 1) To get value from a tuple 
    
print(fruits1[1])

    #2) Tuples you can't change a value

    #3) Delet tuple
'''You can use the del method'''
# del fruits2

# print(fruits2)# When he says fruits is not defined it means it is completely deleted

    #4) Lengths of the fruits
print(len(fruits2))

