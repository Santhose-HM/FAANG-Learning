# Tuple Packing and Unpacking
# Concatenation - +
# Repitation - *
# Packing and Unpacking - *
# Membership - in/not in


# Concatenation
t1 = (1,2,4,5,)
t2 = (2,5,4,1,4)
t3 = t1+t2
print(t3)


# Repitation
t4 = t1*4
print(t4)


# Packing and Unpacking
t1 = 23,34,13,54,23
# Assing mulitple values to one variable is called packing
print(t1)
print(type(t1))

#  Assign multiple varaibles to one tuple is called unpacking
a,b,c,d,e = t1
print(a,b,c,d,e)


t1 = 0,133,34,23,34
a,b,*c = t1
print(a,b,c)


# in and not -in
if 0 in t1:
    print("Yes")
if 0 not in t1:
    print("Yes")
else:
    print("No")