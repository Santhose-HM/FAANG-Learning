# Multiple Returns
# We can return multiple values in any type by using ,
# It will return value as tuple``

def fun(a,b,c):
    sum = a+b+c
    product = a*b*c
    return sum,product


res = fun(10,20,30)
print(res)