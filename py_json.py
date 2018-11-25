# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary
import json

userJSON = '{"firstname": "John", "lastname": "Doe", "age": 30}'

user = json.loads(userJSON)

print(user)
print(user['firstname'])

car = {'make': 'Ford', 'model': 'Mustang', 'year': 1970}

carJson = json.dumps(car)

print(carJson)