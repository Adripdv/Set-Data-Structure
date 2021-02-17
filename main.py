# Set are enclose in curly brackets 
# Set is unordered (no indexing)
# Set is mutable, can contain only immutable items e.g. tuple, strings
# Set elements are unique


''' Python Set Attributes '''

# print(dir(set))

''' Creating Python Sets '''

# set = {} # not a set, is a dictonary 
# set = set() # empty set 
# print(type(set))

# set = {1,2,3}
# print(set)

''' Modifying a Set in Python '''

set_example = {'hello', 'world'}
# # set_example[0] # TypeError: 'set' object is not subscriptable
# set_example.add('yay')
# set_example.add(['hey']) # TypeError: unhashable type: 'list' - set it can only hold immutable items 

# print(help(set.update))

# set_example.update([1,2,3])
# set_example.update('Bitter') # why it separates the letters?
# set_example.update([1,2])
# set_example.update(['1,2'])
# print(set_example)

''' Removing elements from a set '''

# set_example = {1,2,3,4,5,6}
# set_example.discard(5)
# set_example.remove(2)

# print(help(set.pop))
# set_example.pop()

# print(set_example)

''' Set union Operations '''

# a = {1,2,3,6,7}
# b = {4,5,6,7,8,9}

# # print(a | b)
# print(a.union(b))


''' Set intercection Operations '''

# a = {1,2,3,6,7}
# b = {4,5,6,7,8,9}

# print(a & b)
# print(a.intersection(b))

''' Set Difference Operations '''

# a = {1,2,3,6,7,9}
# b = {4,5,6,7,8,9}

# print(a - b) 
# print(a.difference(b)) 

# print(b - a)
# print(b.difference(a))

''' Set Symmetric Difference '''

a = {1,2,3,6,7,9,11,12}
b = {4,5,6,7,8,9,10,11}

print(a ^ b)
print(a.symmetric_difference(b))