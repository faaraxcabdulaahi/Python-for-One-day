# Variable is a container for a value, which can be various types.

'''
This is a 
multiline comment 
or docstring (WHICH IS USED TO DEFINE A FUNCTIONS PURPOSE)
can be a single or double quotes

'''

"""
VARIABLE RULES :
    1. Variable names are case sensitive (name and NAME are differen)
    2. Must start with a letter or an underscore
    3. Can have numbers but can not start with one of them
"""

x = 1           # int (variable type)
y = 3.4         # flaot
name = 'faarax'   # str    
is_cool = True  #bool (The true must be capital letter) 



# Multiple assignment
x, y , name, is_cool = (1,2.4,'faarax',True)

print(x,y, name, is_cool)

#Basic math
a = x + y
print(x,y, name, is_cool,a)

# Checking the type of and we will use type function
print(type(x))

# casting x integer to string
x = str(x)
print(type(x))


y = int(y)
print(type(y))
print(y)

 