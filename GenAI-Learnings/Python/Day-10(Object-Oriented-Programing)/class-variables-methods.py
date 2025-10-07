# Class Variables and Methods

# Class variables are also called as static variables

class Rectangle:
    # In Python we must need to define our properties inisde the __init__ method
    # self - refers current object
    # Below is the example of class variable which is declare anywhere inisde the class
    count = 0
    def __init__(self):
        self.length = 10
        self.breadth = 20
        # This way we can access the class variables inside the instance method
        Rectangle.count +=1

    def area(self):
        return self.length*self.breadth

    def perimeter(self):
        return 2*(self.length+self.breadth)
    # Class methods - It gets class as a parameter
    @classmethod # This makes the method as class method
    def get_count(cls):
        return cls.count


# In this even if I create 2 seperate objects the class variables are common so both instances/objects can access

r1 = Rectangle()
print(Rectangle.get_count())
r2 = Rectangle()
print(Rectangle.get_count())

