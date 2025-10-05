# Maths Built in Functions

# abs(x,/) - It gives postive value no sign unsigned value for integers and folat and for complex numbers it will give magnitude
a = -70
b = 3+4j
print(abs(a))
print(abs(b))

# pow(base,exp,mod=Mode,/)
print(pow(10,2,3))

# round(number,ndigits=None) - For round it takes the nearest even number
print(round(12.67))

# divmod(a,b,/) - Division as well as modulus gives both result
print(divmod(10,3))

# min(iterable,*,key=None,default=None)
print(min([10,3,4,7,2,10,-4,-3,-1,0],key=abs,default='Not Found'))

# max(iterable,*,key=None,default=None)
print(max([10,3,4,7,2,10,-4,-3,-1,0],key=abs,default='Not Found'))

# sum(iterable,start = 0,/) - start add all data ans sum with start
print(sum([10,3,4,7,2,10,-4,-3,-1,0],start=3))

# eval(expression,globals=None,locals=None)
global_dict = {'x':1,'y':2}
local_dict = {'z':5}
print(eval("10+20*4-5"))
print(eval("x+y+z",global_dict,local_dict))


