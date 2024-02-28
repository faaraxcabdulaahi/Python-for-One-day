# A classes is like a blueprint for creating objects. An object has properties and methods (functions) associated with it. Almost everything in python is object. 

# creating class
class User:
    #constructor
    def __init__(self, name, email,age):
        self.name = name
        self.email = email
        self.age = age
        
    # Creating a method associated with this
    
    def greeting(self):
        return f'My name is{self.name} and Iam {self.age}'
        
    #Extend class
class Customer(User):
    #constructor
    def __init__(self, name, email,age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0
    def set_balance(self, balance):
        self.balance = balance
    def greeting(self):
        return f'My name is{self.name} and Iam {self.age} and my balance is {self.balance}'
        
#Init user object
brad = User('Brad Traversy the name of the coarse lecturer', 'brad@gmail.com',88)

print(brad.greeting())


print(type(brad)) # It will print this is a user object

'''Acessing any property'''

#Initialising a customer =object
janet = Customer('janet johnson','janet@gmail.com',65)
janet.set_balance(500)
print(janet.greeting())

print(brad.greeting())

