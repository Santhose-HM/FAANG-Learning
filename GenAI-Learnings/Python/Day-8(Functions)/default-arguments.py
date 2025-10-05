# Default Arguments

# Example - index() in list paramenters element.start,end -> looks like this index(element,start,end) -> element is mandatory start has default value 0 and end has default argument len(list)

def volume(length = 0,breadth =0,height =0):
    vol = length*breadth*height
    return vol

res = volume() # This will return 0 why the default value of lenght,breadth and height is zero so it will return 0 by apply formula
print("The volume is : ",res)


# Fill from right side 
# We can have any type of data while passing argument and taken any type of argument
# Default arguments only once for the first time