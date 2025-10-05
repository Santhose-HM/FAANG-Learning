# Nested Functions


def Outer():
    def Inner():
        print("Inner")
    print("Outer")
    Inner()

Outer()


def totalArea(l,b,h):
    def area(d1,d2):
        return d1*d2
    return 2*(area(l,b)+area(b,h)+area(l,h))

print(totalArea(10,5,3))