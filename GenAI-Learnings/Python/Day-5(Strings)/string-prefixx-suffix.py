# Prefix and Suffix

# startswith(prefix,start,end) - true/false
# endswith(suffix,start,end) - true/false
# removeprefix(prefix) - string
# removesuffix(suffix) - string
# partition(sep) - parition of string in tuple
# rpartition(sep) - reverse partition in tuple


s1 = 'python is very easy'

# startswith()
print(s1.startswith('python'))
print(s1.startswith('is',7))

# endswith()
print(s1.endswith('easy'))
print(s1.endswith('python'))


# removeprefix
print(s1)
new_s1 = s1.removeprefix('py')
print(new_s1)
print(s1)
new_s2 = s1.removeprefix('java')
print(new_s1)

# removesuffix
print(s1)
new_s1 = s1.removesuffix('sy')
print(new_s1)
print(s1)
new_s2 = s1.removesuffix('no')
print(new_s1)


# partition()
new_s3 = s1.partition('is')
print(new_s3)


# rpartition()
new_s4 = s1.rpartition('s')
print(new_s4)
