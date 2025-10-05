# Iterators and Generators

#Iterator

# Built-in Function  iter() - gives iterator on any iterable variable
# next() - move iterator to the next element
# For loop bound in range but it will use we can have more controll like that
# If we access after finsih gives Stop Iteration error
# It will work on set but can't said it will give first element in set because it is unorderd
# It will work on dictionary but only gives the key 
# It will works on  string also
# It will works on range(),list,tuple,dictionary,set

L = [5,6,10,11,15]
i = iter(L)
res = next(i)
print(res)




# Generators
# r = range(4)  object of the range 
# yeild - it will return value within the loop only
# When you are writing your own generator we can directly use next without using iter

def myrange(n):
    i = 0
    while i < n:
        yield i
        i+=1

res = myrange(5)
print(next(res))



days = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat']


def day():
    i = 0
    while True:
        yield days[i]
        i= (i+1)%7


d = day()
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))
print(next(d))

