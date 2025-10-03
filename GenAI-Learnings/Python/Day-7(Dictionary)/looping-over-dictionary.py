# Dictonary Loop Over 

d1 = {1:'One',2:'Two',3:'Three'}

# Keys()
for x in d1.keys():
    print(x,end=',')
print()

# Values()
for x in d1.values():
    print(x,end=',')
print()

# items()
for x in d1.items():
    # Return list of tuples
    print(x,end=',')
print()

# get(key,alt_value)
# It will not give error if key is not found
print(d1.get(3))
# with alt_value if value is not there it will give the alt_value but not added in the dictionary
print(d1.get(5,'Missing'))

# setdefault(key,alt_value)
print(d1.setdefault(3))

# For the key not present
# print(d1.setdefault(5)) - for this it will set none
print(d1)
print(d1.setdefault(5,'Five')) # for this it will give 5: 'Five'
print(d1)