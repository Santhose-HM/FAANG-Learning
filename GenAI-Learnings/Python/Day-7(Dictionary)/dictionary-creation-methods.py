# Dictionary Creation Methods

# d1 = {1:'One',2:'Two',3:'Three'}


# Iterable pairs
dic_tup = [(1,'One'),(2,'Two'),(3,'Three')]
d1 = dict(dic_tup)
print(d1)

# zip functions
key_list = [1,2,3]
values_list = ['One','Two','Three']
print(dict(zip(key_list,values_list)))

# enumerate functions
values = ['One','Two','Three']
# It gives values with index
d = dict(list(enumerate(values,start=1)))
print(d)