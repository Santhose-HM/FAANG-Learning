# Exceptional handling

# try,except,else,finally


a ,b = 10,5

try :
    c =a//b
    print(c)
except:
    print("b should not be zero")

print('End of the program')



l = [10,20,43,23]
index = int(input("Enter the index value : "))

try:
    print(l[index])
except:
    print("Index out of bounds/range")

print("End of the program")