n = int(input("Enter a number : "))

# Pattern one
for i in range(1,n+1):
    for j in range(1,n+1):
        if i>=j:
            print("*",end="")
    print("")

print("")

# Pattern two
for i in range(1,n+1):
    for j in range(1,n+1):
        if i<=j:
            print("*",end="")
    print("")


print("")

# Pattern three
for i in range(1,n+1):
    for j in range(n+1,0,-1):
        if i>=j:
            print("*",end="")
        else:
             print(end=" ")
            
    print("")

print("")

# Pattern four
for i in range(1,n+1):
    for j in range(1,n+1):
        if i>j:32
            print(end=" ")
        else:
            print("*",end="")
    print("")


