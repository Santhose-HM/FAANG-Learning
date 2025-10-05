# Function as Parameter

def welcome():
    print('welcome')

def fun(f):
    f()

fun(welcome)




def add(x,y):
    return x+y

def sub(x,y):
    return x-y


def arthimetic(f,x,y):
    return f(x,y)


res = arthimetic(add,10,5)
print(res)
res = arthimetic(sub,10,5)
print(res)