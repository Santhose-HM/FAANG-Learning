# Dictionary-Methods
d1 = {1:'One',2:'Two',3:'Three',4:'Four'}
d2 = {5:'Five'}
lis = [1,2,3,4]
# update(dictionary)
d1.update(d2)
print(d1)

# fromkeys(squence,default)
print(dict.fromkeys(lis,'Unknown')) # static methods

# copy()
di = d1.copy()
print(di)

# pop() - Takes input as key value and remove particular key value pair
d1.pop(1)
print(d1)

# popiten() - This will remove the last element in the dictionary
d1.popitem()
print(d1)

# clear() - Empty the dictionary
d1.clear()
print(d1)