# Set operations

s1 = {1,2,3,5,7}
s2 = {5,7,9,10,11}

# Union
s3 = s1.union(s2)
print(s3)

# Intersection
s4 = s1.intersection(s2)
print(s4)

# Intersection Update
# print(s1)
# s1.intersection_update(s2)
# print(s1)

# Difference
s5 = s1.difference(s2)
print(s5)
s6 = s2.difference(s1)
print(s6)

# Difference Update
# s1.difference_update(s2)
# print(s1)
# s2.difference_update(s1)
# print(s2)

# Symmetric Difference
s7 = s1.symmetric_difference(s2)
print(s7)
s8 = s2.symmetric_difference(s1)
print(s8)

# Symmetric Difference Update
# s1.symmetric_difference_update(s2)
# print(s1)
# s2.symmetric_difference_update(s1)
# print(s2)