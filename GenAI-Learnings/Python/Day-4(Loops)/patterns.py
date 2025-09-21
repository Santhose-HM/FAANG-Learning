# Patterns



# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * *
for i in range (1,6):
    for j in range(1,6):
        print("*",end = " ")
    print()
print()

print("==============================")

# * 
# * * 
# * * * 
# * * * * 
# * * * * *
# Method 1
for i in range(1,6):
    for j in range(1,6):
        if i>=j:
            print("*",end=" ")
    print()
print("==============================")
# Method 2
for i in range(1,6):
    for j in range(1,i+1):
            print("*",end=" ")
    print()

print("==============================")

# * * * * * 
# * * * * 
# * * * 
# * * 
# * 
# Method 1
for i in range(1,6):
    for j in range(1,6):
        if i<=j:
            print("*",end=" ")
    print()
print("==============================")
# Method 2
for i in range(1,6):
    for j in range(1,6-(i-1)):
        print("*",end=" ")
    print()
print("==============================")

# *****
#  ****
#   ***
#    **
#     *

# Method 1
for i in range(1,6):
    for j in range(1,6):
        if i>j:
            print(" ",end="")
        else:
            print("*",end="")
    print()

