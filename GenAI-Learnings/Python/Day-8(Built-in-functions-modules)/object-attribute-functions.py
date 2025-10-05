# Object & Attribute Built-in Functions
import math

# type(object,bases=None,dict=None)
print(type(10))
print(type('hello'))
print(type(12.34))
print(type([1,2,3,4]))

# isinstance(object,classinfo,/) - to check the particular object belongs/instance to the class and return boolean
x = 10
print(isinstance(x,int))
print(isinstance(x,float))
print(isinstance(x,(int,float)))

# hasattr(object,attribute) - The particular object has the attribute/method in class or not  - return boolean result
text= 'Hello'
print(hasattr(text,'lower'))

# getattr(object,attribute,default) - We can get reference of particular attribute from the module
print(getattr(math,'pi'))
print(getattr(math,'sqrt')(25))


# id(object,/) - Id for any object
x = 10
y = 2
print(id(x))
print(id(y))

# dir(object=None,/) - gives all the members of class/module
print(dir(list))
print(dir(math))


# repr(object) - gives actual representation of the data
text = 'Hello World'
print(repr(text))