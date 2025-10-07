# Object Oriented Programming

# Creating a Python class for Rectangle
class Rectangle:
    # In Python we must need to define our properties inisde the __init__ method
    # self - refers current object
    def __init__(self):
        self.length = 10
        self.breadth = 20

    def area(self):
        return self.length*self.breadth

    def perimeter(self):
        return 2*(self.length+self.breadth)


# Creating Object

rectangle = Rectangle()

# Accessing the properties and methods using Object

print("Length of the rectangle : ",rectangle.length)
print("Breadth of the rectangle : ",rectangle.breadth)

area_of_rectangle = rectangle.area()
perimeter_of_rectangle = rectangle.perimeter()

print("Area of Rectangle : ",area_of_rectangle)
print("Perimeter of Rectangle : ",rectangle.perimeter())