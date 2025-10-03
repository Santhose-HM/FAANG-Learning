# Set Introduction
# Collection of values
# It is concepts in Mathmetics
# Does not have indexing, slicingare not done and doesn't allow the Duplicates
# It is also a Data Structure

# Creating set
l1 = {1,2,3,4,5,6}
print(l1)
print(type(l1))

# Duplicates not allowed
l2 = {1,1,2,2,3,3,4,5,6}
print(l2)
print(type(l2))

# Contain any type of data
l3 = {1,2,True,23.43,5+6j}
print(l3)
print(type(l3))

# unordered
for x in l3:
    print(x,end=",")
print()
# Types of creating set
s1 = set([1,23,46,42])
print(s1)
print(type(s1))

# string iterable
s1 = set('python')
print(s1)
print(type(s1))

# single element
s1 = {4}
print(s1)
print(type(s1))


# muttable

s1 = {1,2,3,4,5}
print(s1)
s1.add(60)
print(s1)


# Different type of data
s1. add("Hai Hello")
print(s1)

# Add the tuple
s1.add((12,343,231,12))
print(s1)

# Add the list
# Error - Unhasble type means only allowed immutable values are allowed to add
# List is muttable so it wil throw error

# Removing elements
s1.remove(60)
print(s1)

# Pop
s1.pop()
print(s1)


# The storing of the set in hash table is using hash functions h(x) = x%10
# So the reason the set is not stored values in order
# Collision also occurs -> which means when 2 values have the same position in hash table
# Time for insertion of one value is O(1) -> constant
# Search is also the value is O(1) - constant



