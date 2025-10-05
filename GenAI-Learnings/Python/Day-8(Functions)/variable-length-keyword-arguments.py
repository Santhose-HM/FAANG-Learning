# Variable length keyword arguments
# For variable length keyword argument we use **kwargs
# It retun the value as dictionary
# keyword is key and then value as value 
# We cannot never have after **kwargs
# Before the **kwargs we can use positional arguments/keyword arguments



def fun(**kwargs):
    print(kwargs)


fun(start =20,stop =30,step =100)