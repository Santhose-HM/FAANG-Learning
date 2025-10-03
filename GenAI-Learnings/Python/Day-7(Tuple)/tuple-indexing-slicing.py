# Indexing and Slicing
# It is immutable so you can only perform read operation only

t1 = (*(x for x in range(1,8)),)
print(t1)

# Accessing/Indexing
print(t1[4])
print(t1[-3])

# Slicing
# Entire tuple
print(t1[:])
# from start only
print(t1[-3:])
# from and end
print(t1[2:5])
# reverse
print(t1[::-1])
print(t1[4::-1])