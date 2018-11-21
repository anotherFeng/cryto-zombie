# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = "Feng"
age = 30
# print('Hello I am ' + name + ' and I am ' + str(age))

# String Formatting
# print('{}, {}, {}'.format('a', 'b', 'c'));

# print('My name is {name} and I am {age}'.format(name='Feng', age='37'));

# F-strings
# print(f'My name is {name} and I am {age}')


# String Methods
s = 'hello there world'

# capitalize
# print(s.capitalize())
# all cap
# print(s.upper())
# print(s.lower())
# print(s.swapcase()) #swap cap to lower and lower to cap.

# print(len(s))

# Replace
# print(s.replace('world', 'everyone'))

#count char
sub = "h"
print(s.count('s')) # count the amount of s inside this string
print(s.startswith('hello')) #true
print(s.endswith('d')) #true
print(s.split()) # split into list
print(s.find('r')) #find position
print(s.isalnum()) #return true if everything is letters or number or mixed
print(sub.isalpha()) #true if all are letters