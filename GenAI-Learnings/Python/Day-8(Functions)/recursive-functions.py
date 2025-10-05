# Recursive Functions - these are alternative to loop
# But loops are  faster than recursive functions

# A function which call itself is called Recursive function
# Base condition is necessary

# Recursive function
def fun(n): 
    if n > 0: # The condition wihich will stop recursion it is called base condtition
        print(n)
        fun(n-1) # Recursive function call

fun(10)



# Factorial of numbers

def fact (n):
    if n<=0:
        return 1
    else:
        return n*fact(n-1)
print(fact(3),end=" ")