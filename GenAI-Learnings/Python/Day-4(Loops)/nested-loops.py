# Nested loops


for i in range(1,5):
    for j in range(1,6,i+1):
        print("*",end=" ")
    print("")
    



# Prime Number between 1 to 100

for i in range(1,100):
    count = 0
    for j in range(1,100):
        if i %j == 0:
            count+=1
    if count == 2:
        print(i,end=" ")
