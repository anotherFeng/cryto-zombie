# A List is a collection which is ordered and changeable. Allows duplicate members.
numbers = [1,2,3,4,5]
print(type(numbers))

fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

print(fruits[1])

print(len(fruits))
fruits.append('Mangos')
fruits.remove('Grapes')

fruits.insert(2, 'Strawberries')
fruits.pop(3)

#reverse list
fruits.reverse()

# sort list
fruits.sort()

#reverse sort
fruits.sort(reverse=True)

print(fruits)
