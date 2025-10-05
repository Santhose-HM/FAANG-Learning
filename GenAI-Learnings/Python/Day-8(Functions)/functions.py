# Function Introduction

# Built-in functions
# range()
# print()
# list()

# User Defined Functions
# def fun(<parameter>)
#       body
#       return result


# Passing values - Actual Parameters/Arguments
# The variables which we used in the header of functions is called Formal Parameters/Arguments

def volume(length,breadth,height):
    vol = length*breadth*height
    return vol

res = volume(10,5,12)
print("The volume is : ",res)


