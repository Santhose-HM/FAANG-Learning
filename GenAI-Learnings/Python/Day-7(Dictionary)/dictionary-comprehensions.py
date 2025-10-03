# Dictionary Comprehensions

# d1 = {1:'One',2:'Two',3:'Three'}

# Iterable pairs
lis = [(1,'One'),(2,'Two'),(3,'Three')]
d1 = {key:value for key, value in lis}
print(d1)

# Zip Functions
key_list = [1,2,3]
values_list = ['One','Two','Three']
li = list(zip(key_list,values_list))
d1 = {key:value for key,value in li}
print(d1)

# Enumerate Functions
values = ['One','Two','Three']
d1 = {key:value for key,value in enumerate(values,start=1)}
print(d1)