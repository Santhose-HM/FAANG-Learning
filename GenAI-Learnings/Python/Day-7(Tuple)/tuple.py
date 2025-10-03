# Tuple
# Tuple is immuatble
# Tuple is another Data Structure
# Duplicates are allowed

# Create a tuple
t1 = (1,2,3,4,5,6)
print(t1)
print(type(t1))

t1 = ('str',123,124.243,True,4+6j)
print(t1)
print(type(t1))

t2 = tuple([1,234,4563,435,43])
print(t2)
print(type(t2))

t2 = ()
print(t2)
print(type(t2))

t3 = (4,)
print(t3)
print(type(t3))

t4 = 12,34,12,53,23,54
print(t4)
print(type(t4))

t5 = tuple(range(1,6))
print(t5)
print(type(t5))


# Accessing element
print(t1[2])


# Traversing
for x in t1:
    print(x,end =",")