# List Comprehensions

# L = [exp for item in iterable]

L = [x for x in range(1,21)]
print(L)


L3 = [x.lower() for x in 'PyThoN']
print(L3)

L4 = [x for x in 'ab*cde7f' if x.isalpha()]
print(L4)