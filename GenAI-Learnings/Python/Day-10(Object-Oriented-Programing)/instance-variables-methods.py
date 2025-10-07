# Instance - Variables and methods

# Variables - Instance,class,static
# Methods - Instance,class,static

#Instance variables are defined with self and the instance methods are defined with self parameter

class Rectangle:
    def __init__(self, l,b):
        # These 2 varaibles are called as the instance variables
        self.length = l
        self.breadth = b
    # These are called as the instance methods
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)


# Ways of creating instance variables
# In the below class we create 2 instance variables one in __init__ method and the fun method
# If I want to use both then I need to create both first right? So the variable which is in the init is automatically created when object is created
# If I really want to use b aslo I want to call the fun() to create it
# It leads to create a two instance variables

class Test:
    def __init__(self):
        self.a = 10
    def fun(self):
        self.b = 20
    def show(self):
        print(self.a)
        print(self.b)
        print(self.c)

t = Test()
t.fun()
# It is not right way to do it
t.c =30
t.show()








