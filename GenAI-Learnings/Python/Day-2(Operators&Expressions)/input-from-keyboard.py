# Taking input from the keyboard - input()
# This input() returns always a string value
# So convert the result of input() with type coversion functions

import math

length = float(input("Enter the length : "))
breadth = float(input("Ente the breadth : "))

area = length*breadth
print("Area of the rectangle is : ",area)




# Surface area of a cuboid

# Formula - 2*(l*h+l*b+b*h)



l = float(input("Enter the length  : "))
b = float(input("Enter the breadth : "))
h = float(input("Enter the height : "))

total_surface_area = 2*((l*b)+(l*h)+(b*h))

print("The total surface area of the cuboid is : ",total_surface_area)



# Quadratic Equations
# ax2+ bx + c = 0


a = int(input("Enter the co-efficent of x square : "))
b = int(input("Enter the co-efficent of x : "))
c = int(input("Enter the co-efficent of constant :  "))

root_one = (-b+math.sqrt(b**2-4*a*c))/(2*a)
root_two = (-b-math.sqrt(b**2-4*a*c))/(2*a)

print("The root one is  : ",root_one)
print("The root two is : ",root_two)



