number = int(input("Enter a number : "))
odd_dig = 0
even_dig = 0
while number!=0:
    rem = number%10
    if rem%2 == 0:
        even_dig+=rem
    else:
        odd_dig+=rem
    number = number//10
print("Sum of Odd digits : ",odd_dig)
print("Sum of Even digits : ",even_dig)
