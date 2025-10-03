# Adding Elements in list

l1 = [12,32,31,43,12]
print(l1)

# append(element)
l1.append(16)
print(l1)

# extend(iterable)
l1.extend([12])
print(l1)
l1.extend([13,412,42,74])
print(l1)

# insert(index,element)
l1.insert(1,10)
print(l1)

# copy()
l2 = l1.copy()
print(l2)
