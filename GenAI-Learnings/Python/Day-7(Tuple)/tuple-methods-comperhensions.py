# Tuple Methods and Comprehensions

# iterable -> t = (*(exp for item in iterable),)

t = (*(item for item in range(1,11)),)
print(t)
print(type(t))
t = tuple(item for item in range(11,21))
print(t)
print(type(t))
