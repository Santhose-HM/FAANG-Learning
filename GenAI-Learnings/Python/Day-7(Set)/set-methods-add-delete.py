# Set Methods Add and Delete
s1 = {10,20,30,40,50}
print(len(s1))

# add(element)
s1.add(60)
print(s1)
print(len(s1))

# update(iterable)
s1.update((40,20,90))
print(s1)
print(len(s1))

# copy()
s2 = s1.copy()
print(s2)
print(len(s2))
print(id(s1))
print(id(s2))


# pop()
s1.pop()
print(s1)
print(len(s1))

# discard(element) - It will not return error if value is not found
s1.discard(90)
print(s1)
print(len(s1))


# remove(element) - It will return error if the value is not found
s1.remove(30)
print(s1)
print(len(s1))

# clear()
s1.clear()
print(s1)
print(len(s1))
