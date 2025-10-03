# Removing Elements

l1 = [12,67,21,98,10]
print(l1)

# pop(index)
l1.pop(1)
print(l1)
l1.pop()
print(l1)

# remove(element) - If the element is not there throws
l1.remove(12)
print(l1)

# clear() - Empty the enitre list
l1.clear()
print(l1)

# del
del l1 # completely delete even with variable declaration