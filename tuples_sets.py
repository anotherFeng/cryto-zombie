# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

#simple tuple
fruit_tuple = ('Apple', 'Orange', 'Mango')
print(fruit_tuple[1])

# not possible
# fruit_tuple[1] = 'Grape'

# tuples with one value should have trailing comma
fruit_tuple_2 = ('Apple',) # otherwise will be a string

print(fruit_tuple)
print(len(fruit_tuple))

del fruit_tuple_2 # can't delete element but can delete the whole tuple

# A Set is a collection which is unordered and unindexed. No duplicate members.
# set is just like a mix of array and tuple except it doesnt allow duplicate value
fruit_set = {'Apple', 'Orange', 'Mango'}
print('Apple' in fruit_set) # check if value is in a set

fruit_set.add('Grape')

fruit_set.remove('Grape')

print(fruit_set)
fruit_set.clear() # clear set
del fruit_set # completely remove it