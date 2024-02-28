# Strings in python is defined a sequence of characters enclosed by single or double quotes. 

name = "faarax"
age = 100

# Concatenate
'''To concatenate means to insert a variable into a string'''

# print('Hello, my name is '+ name +'and I am' + age) # Here you will get an error because we can only concatenate strings.
 # if you want it to work you have to cast it to the str
# print('Hello, my name is '+ name +'and I am ' + str(age))

#-----------------
#String Formatting
#-----------------
'''
We can do string formatting and Two ways is by string formatting
'''
    # Way 1 :Arguments by position
print('My name is {name} and I am {age} '. format (name=name , age=age))

# { } This curly braces in the print functions are called PLACE HOLDERS.

    # Way 2: F- String (Available in python 3.6+)
print(f'Hello my name is {name} and I am {age}')

#--------------
#String Methods
#--------------

s = 'Hello world'

    # 1= Capitalize string
'''Here we will use a method called CAPITALIZE'''
print(s.capitalize())

    # 2= Make all uppercase
print(s.upper())

    # 3= Make all lower
print(s.lower())

    # 4= Swap case
'''Makes first letter small and all letters after the first letter CAPITAL'''
print(s.swapcase())

    # 5= Get length
'''Is a function used in ant data type and he gets the length'''
print(len(s))

    # 6= Replace
print(s.replace('world','everyone'))

    # 7= count 
sub = 'h'
print(s.count(sub))

    # 8= Starts with
print(s.startswith('Hello'))

    # 9= Ends with
print(s.endswith('d'))

    # 10= split into a list  (it is array)
print(s.split())
'''This one splits hello world into a list'''

    #11= find position
print(s.find('r'))

    #12= is all alphanumeric
print(s.isalnum())

    #13= is alphabetic
print(s.isalpha())

    #14= is all numeric
print(s.isnumeric())

'''The last will be false and the reason for that because of the SPACE'''

y = 'Helloworld'

#12= is all alphanumeric
print(y.isalnum())

    #13= is alphabetic
print(y.isalpha())

    #14= is all numeric
print(y.isnumeric())

"""If you get rid of that space it will be TRUE in (alpha and alphanumeric)"""

'''And numeric it's going to be false'''

