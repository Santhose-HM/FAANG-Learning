# Property Methods
class Rectangle:
    # In Python we must need to define our properties inisde the __init__ method
    # self - refers current object
    def __init__(self,l,b):
        self.length = l
        self.breadth = b
    # Getters and setter for length
    @property
    def length(self):
        return self._length
    @length.setter
    def length(self,l):
        if l>=0:
            self._length = l
        else :
            self._length = 0
    # Getter and setters for breadth
    @property
    def breadth(self):
        return self._breadth
    @breadth.setter
    def breadth(self,b):
        if b>=0:
            self._breadth = b
        else :
            self._breath = 0
    def area(self):
        return self.length*self.breadth

r1 = Rectangle(10,3)
r1.length = 20
print(r1.length)