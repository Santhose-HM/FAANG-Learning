# Function as Object

print(print.__name__)

# You can assign a function to the variable also
show = print
show('Hello')

take = input
var = int(take("Enter the number : "))
show(var)


# Own function

def fun():
    print('My Function')

f = fun
f()