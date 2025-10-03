# Index ad Sorting

l1 = [12,34,45,64,89,12,12]

# index(element,start,end) - it will show first occurance if we not mention start and end
print(l1.index(64,1,4))

# count(element)
print(l1.count(12))

# reverse()
l1.reverse()
print(l1)

# sort(*,key=None,reverse=False)
l1.sort()
print(l1)
