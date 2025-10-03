# Set Operators
s1 = {1,2,3,5,7}
s2 = {5,7,9,10,11}
# Union - |
s3 = s1|s2
print(s3)

# Intersection - &
s4 = s1&s2
print(s4)

# Intersection update - &=
# print(s1)
# s1&=s2
# print(s1)

# Difference - '-'
s5 = s1-s2
print(s5)
s6 = s2-s1
print(s6)

# Difference Update - '-='
# s1-=s2
# print(s1)
# s2-=s1
# print(s2)

# Symetric Difference - ^
s7 = s1^s2
print(s7)
s8 = s2^s1
print(s8)

# Symetric Difference Update - ^=
# s1^=s2
# print(s1)
# s2^=s1
# print(s2)