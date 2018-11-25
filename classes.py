# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

class User:
  def __init__(self, name, email, age):
    self.name = name
    self.email = email
    self.age = age

  def greeting(self):
    return f'My name is {self.name} and I am {self.age}'

  def has_birthday(self):
    self.age += 1

class Customer(User):
  def __init__(self, name, email, age):
    self.name = name
    self.email = email
    self.age = age
    self.balance = 0

  def set_balance(self, balance):
    self.balance = balance
    # return super().__init__(name, email, age)
  
  def greeting(self):
    return f'My name is {self.name} and I am {self.age} and I owe a balance of {self.balance}'

brad = User('Brad', 'brad@gmail.com', 37)

brad.has_birthday()

print(brad.age)
print(brad.greeting())

john = Customer('John', 'john@gmail.com', 40)
john.set_balance(500)

print(john.greeting())