# JSON is commonly used with data APIS . Here how we can parse JSON into a python dictionary.

# There is a module that we can use which is callesd json, that we can import. 

import json

# Sample JSON
userJSON = '{"first_name":"faarax", "last_name": "cali", "age": 77}'

#Parse to dict
user = json.loads(userJSON)
print(user) # Here it gives the dictionary of the user

print(user['first_name'])


#Take a dictionary and turn into a JSON format

car = {'make': 'Ford','model':'Mustang','year':1970}
carJSON = json.dumps(car)
print(carJSON)

"""




   ALXAMDULILAAH KOORSADII 95 DAQIIQO AHAYD WAAN DHAMEEYAY



"""