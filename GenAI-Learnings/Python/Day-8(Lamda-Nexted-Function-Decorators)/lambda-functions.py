# Lamda Functions - Anonymous Functions , Simple Functions, Single line Functions
# It doesn't have function name
# Useful for Functional Programming
# Assign it to the variable

def double(x):
    return x*2

# Convert above function into lamda function

k = lambda x: x*2
print(double(2))
print(k(2))



add = lambda x,y:x+y

print(add(10,5))


l = [1,2,3,4,5,6,7,8,9,10]
f = filter(lambda x : x%3==0,l) # It will get filtered data from iterable

print(list(f))



k = lambda x:x if x%2==0 else -x
l2 = list(map(k,l))
print(l2)


l1 = [[4,2,'Six'],[1,4,'Five'],[2,2,'Four']]
l2 = sorted(l1,key=lambda x :x[0]+x[1])
print(l2)
