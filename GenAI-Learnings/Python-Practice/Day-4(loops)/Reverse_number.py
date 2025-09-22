number = int(input("Enter a number : "))

sum = 0
while number!=0:
    rem = number%10
    sum = (sum*10)+rem
    number=number//10
print(sum)
