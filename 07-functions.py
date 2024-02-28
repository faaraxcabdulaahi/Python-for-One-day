# A function is a block of code which only runs when it is called. 

#In python we donot use curly brackets, we use identation with taps or spaces.

#1) Create function

def sayHello(name):
    print(f'Hello {name}')
sayHello('Faarax cabdulaahi')

#2) Default parameters or arguments

def sayHello(name='Faarax cabdulaahi'):
    print(f'Hello {name}')
sayHello()

#3) Return value

def getSum(num1,num2):
    total = num1 + num2 # This is a variable within a function scope
    #This is callled <GLOBAL SCOPE> function because we have written the function within function scope.
    
    return total

print(getSum(3,4)) # Out put is 7

'''Or you can make a variable'''

num = getSum(3,4)
print(num) # And this one output is 7

