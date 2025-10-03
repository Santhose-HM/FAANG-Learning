# Dictionary Introduction - Key value pairs
# Using Key we can easily search the values 
# Keys will be unique
# Values may be duplicate

# Create a Dictionary

d1 = {} #-> Empty curly braces it will take a dictionary
print(type(d1))

d1 = {1:'One',2:'Two',3:'Three',4:'Four'}
print(d1)
print(type(d1))


# Reading - using key we can read the data

print(d1[1])

# If the key is not there gives error
# print(d1[5])

# Update
d1[3] = 'Five'
print(d1)


# add new value
d1[5] = 'New data'
print(d1)


# Traversing
for i in d1:
    # Just print key
    # print(i)
    # This will get the values
    print(d1[i])

# Key and value can be any type
d = {1:23.3,2.5:True,5+6j:'Sample'}
print(d)
print(type(d))

# Hold any Data Structure(list,tuple,set and dictionary) as the key values
dic ={1:[2,32,4],2:(1,2,4),3:{12,342,54},4:{1:1,2:2}}
print(dic)
print(type(dic))

# Hold tuple like only immutable types can be used as key
di = {(1,2):'Hi'}
print(di)
print(type(di))

