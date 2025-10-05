# Nested Exception 


l  = [10,203,42]

try:
    try:
        index = int(input("Enter Index : "))
    except ValueError as e:
        print(e)
    else:
        print(l[index])
except IndexError as e:
    print(e)
