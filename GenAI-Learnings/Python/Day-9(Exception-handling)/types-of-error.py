# Types of error

# Syntax Error
a = input("Enter Value of A : ")
# b = input("Enter Value of B : ) - It is a syntax error(Typing Mistake)

# Logical Error
b = input("Enter the input of B :")
if a>b:
    print(a)
else:
    print(a) # It is logical error (Error on writing the logic)


# Runtime Error

c = a//b # Run time Error(inputs are string but is works on integer )
print(c)