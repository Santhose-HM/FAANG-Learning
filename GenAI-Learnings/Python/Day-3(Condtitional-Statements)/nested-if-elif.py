# Nested  if and elif

# Temperatrue Check


temp = float(input("Enter the temperature : "))

if temp == 25:
    print("Normal")
else:
    if(temp<24):
        print("Cold")
    else:
        print("Hot")



if temp == 25:
    print("Normal")
elif temp < 24:
    print("Cold")
else:
    print("Hot")



# Generate Discounted Bill


amount = int(input("Enter the amount"))

if amount < 1000:
    amount = amount - amount*0.1
    print("10% discount : ",amount)
elif amount >= 1000 and amount< 5000:
    amount = amount - amount*0.15
    print("15% discount : ",amount)
elif amount >= 5000 and amount < 10000:
    amount = amount - amount*0.2
    print("20% discount : ",amount)
else:
    amount = amount - amount*0.25
    print("25% discount : ",amount)



# Day number to name

day_number = int(input("Enter the day number : "))
if day_number == 0:
    print("Monday")
elif day_number == 1:
    print("Tuesday")
elif day_number == 2:
    print("Wednesday")
elif day_number == 3:
    print("Thrusday")
elif day_number == 4:
    print("Friday")
elif day_number == 5:
    print("Saturday")
elif day_number == 6:
    print("Sunday")
else :
    print("Invalid day number")


# Month Number to name

month_number = int(input("Enter the month number :  "))
if month_number == 0:
    print("January")
elif month_number == 1:
    print("Feburary")
elif month_number == 2:
    print("March")
elif month_number == 3:
    print("Apirl")
elif month_number == 4:
    print("May")
elif month_number == 5:
    print("June")
elif month_number == 6:
    print("July")
elif month_number == 7:
    print("August")
elif month_number == 8:
    print("September")
elif month_number == 9:
    print("October")
elif month_number == 10:
    print("November")
elif month_number == 11:
    print("December")
else:
    print("Invalid Month")


# Digit to number
digit = int(input("Enter the digit : "))

if digit == 0:
    print("zero")
elif digit == 1:
    print("one")
elif digit == 2:
    print("two")
elif digit == 3:
    print("three")
elif digit == 4:
    print("four")
elif digit == 5:
    print("five")
elif digit == 6:
    print("six")
elif digit == 7:
    print("seven")
elif digit == 8:
    print("eight")
elif digit == 9:
    print("nine")
else:
    print("Invalid digit")

# Leap Year

year = int(input("Enter the year : "))
if year%100 == 0 :
    if year%400 == 0:
        print("Leap Year")
    else:
        print("Not a Leap Year")
elif year% 4 ==0:
    print("Leap Year")
else :
    print("Not a leap year")



