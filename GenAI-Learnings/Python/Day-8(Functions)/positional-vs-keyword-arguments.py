# Positional Vs Keyword Arguments


# Positional Argument - The value 10 is goes to length, similarly for breadth and height it goes based on position of parameter(Pass in same order)
def volume(length,breadth,height):
    print(length,breadth,height)
    vol = length*breadth*height
    return vol

# res = volume(10,5,12) - This will pass on position
res = volume(length=10,breadth=30,height=100) # This will pass baed on the keyword 
print("The volume is : ",res)


# Keyword Arguments - By giving the keyword and assign them into to value while pass is called keyword arguments (Pass in any order)

# You can pass both positional and keyword in same function
# Positional Argument first and keyword Argument in the function

# Samples
# v = volume(10,b=5,h=3) - Correct
# v = volume(10,b=5,3) - Worng
# v = volume(l=10,5,k=3) - Worng
# v = volume(10,5,b=3) - Worng