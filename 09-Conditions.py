# If / Else conditions are used to decide to do something being true or false

x = 3
y = 3



#1- Comparison Operaters (==. !=, >, <, >=, <=)

#-----------
#A)Simple If
#-----------

if x > y: # The you indent the next line
    print(f'{x} is greater than {y}')
    
#---------
#B)If/Else
#---------

if x >y :
    print(f'{x} is greater than {y}')
else:
    print(f'{y} is greater than {x}')

#-------  
#C) elif
#-------

if x >y :
    print(f'{x} is greater than {y}')
elif x == y: #This elif needs a condition
    # To output this condition the two varible must to be similar. 
    print(f'{x} is uqual to {y}')
else:
    print(f'{y} is greater than {x}')
    
#------------
#D) Nested if
#------------
if x > 2:
    if x <= 10:
        print(f'{x} is greater than 2 and less than or equal to 10')


#2-Logical operaters (and, or, not)- Is used to combine conditional statements

#1=And 
'''This two if must be true'''

if x > 2 and x <= 10:
    print(f'{x} is greater than 2 and less than or equal to 10')
    
#2=Or
'''This one if must be true'''

if x > 2 or x <= 10:
    print(f'{x} id not equal to 10')

#3=Not
'''This the two if must be false'''


#3- Membership Operaters(not, not in) - Membership operaters are used to test if a sequence is presented in an object

    #a=in
numbers = [1,2,3,4,5]
if x in numbers:
    print(x in numbers)
    
    #b=not in
if y not in numbers:
    print(x not in numbers)
    

#4- Identatity Operaters (is, is not)- Is used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location :

    #a= is 
'''The output is true if the 2 variables have equal value'''
d = 34
t = 34
if d is t:
    print(d is t)
    
    #b= is not 
'''The output is true if the 2 variables have not equal value'''
d = 34
t = 45
if d is not t:
    print(d is not t)
    


