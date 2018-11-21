# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# Simple dict
person = {
  'first_name': 'Feng',
  'last_name': 'Chen',
  'age': 30
}

# constructor way
# person = dict(
#   first_name= 'Feng',
#   last_name= 'Chen',
#   age= 30
# )

print(person['first_name'])
print(person.get('last_name'))

person['phone'] = '555-555-5555'

#get keys
print(person.keys())

#get tuples of each entry
print(person.items())

#make copy
person2 = person.copy()
person2['city'] = 'Boston'
print(person2)

del(person['age'])  #Same as below
person.pop('phone') #

print(len(person2)) # print length of entry for dic

print(person)

people = [
  {'name': 'Martha', 'age': 40},
  {'name': 'Bob', 'age': 20},
]

print(people)
print(people[0]) #gives us Martha
print(people[0]['age']) #gives us 40