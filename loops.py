# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people = ['John', 'Will', 'Janet', 'Karen']

# for person in people:
#   print('current person: ', person)
#   if person == 'Janet':
#     break


for person in people:
  if person == 'Janet':
    continue # will skip janet
  print('current person: ', person)

for i in range(len(people)):
  print('Current person:', people[i])

for i in range(0, 10):
  print('Number', i)

# While loops execute a set of statements as long as a condition is true.
count = 0
while count <= 10:
  print('Count: ', count)
  count += 1