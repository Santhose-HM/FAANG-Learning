# Indexing

s1 = "Hello World"
print(s1[2])
print(s1[-2])
# Strings are immutable so we can't change its character/length
# If we done changes give new string

# String Slicing "[start:stop:steps]"


print(s1[1:7])

# If we don't give string it takes 0 if I not give the stop it will give upto last
# If we didn't give both the start and stop by just : then it gives entire string


print(s1[:])

# Negative indexes
print(s1[-5:])

print(s1[-5:-2])


# By default it will take step 1
print(s1[0:11:2])


s2 = s1[::]


print(s2)
print(s2[::-1])


