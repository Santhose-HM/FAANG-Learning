# Constructor and self
# self is reference to the current object

class Rectangle:
    # In Python we must need to define our properties inisde the __init__ method
    # self - refers current object
    # If I want to give my own arguments I need to make the constructor to get and make use of it like this 
    def __init__(self,length =1,breadth =1):
        print(id(self))
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length*self.breadth

    def perimeter(self):
        return 2*(self.length+self.breadth)


# When I write this line the __init__ method is called and created an object
# In Python this __init__ method is consider as constructor
rectangle = Rectangle(15,8) # In this if I pass the length and breadth as parameter it will create an object with that parameter
print(id(rectangle))

print("Length of the rectangle : ",rectangle.length)
print("Breadth of the rectangle : ",rectangle.breadth)

area_of_rectangle = rectangle.area()
perimeter_of_rectangle = rectangle.perimeter()

print("Area of Rectangle : ",area_of_rectangle)
print("Perimeter of Rectangle : ",rectangle.perimeter())
