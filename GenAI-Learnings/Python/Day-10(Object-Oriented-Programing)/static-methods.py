# Static methods

class Rectangle:
    # In Python we must need to define our properties inisde the __init__ method
    # self - refers current object
    def __init__(self,):
        self.length = 10
        self.breadth = 20

    def area(self):
        return self.length*self.breadth

    def perimeter(self):
        return 2*(self.length+self.breadth)

    @staticmethod
    def calc_area(length,breadth):
        return length*breadth


print(Rectangle.calc_area(20,40))
