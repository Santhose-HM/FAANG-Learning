# List indexing and slicing

# Reading using Indexing
l1 = [2,342,34,2342,52,563]
print(l1[3])
print(l1[-3])


# Reading using slicing
print(l1[1:4:2])
print(l1[-5:-2:2])


# Writing using index
l1[3] = 10
print(l1)

# l1 [2] = [10,23] it is also possible

# Writing using slicing
l1[1:4] = [1,24,32,134,52,12,53]
print(l1)

l1[1:4:2] = [100,200]
print(l1)
