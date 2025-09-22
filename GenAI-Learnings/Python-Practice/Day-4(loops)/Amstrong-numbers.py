number = int(input("Enter a number : "))
original = number
ams = 0
while number!=0:
    rem = number%10
    ams = ams+(rem**3)
    number = number//10

if ams == original:
    print("Amstrong")
else:
    print("Not an Anstrong")
