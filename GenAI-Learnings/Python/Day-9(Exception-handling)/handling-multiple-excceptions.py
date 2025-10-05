# Handle Multiple Exceptions

l =[10,30,32]
try:
    index = int(input("Enter the index : "))
    print(l[index])

except (IndexError,TypeError,ValueError) as msg:
    print(msg)