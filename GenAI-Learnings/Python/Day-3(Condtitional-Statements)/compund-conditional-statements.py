# Compound Conditional Statements

# Logical operators with Truth Table

# and, or, not - They gave results in boolean format

# and - both conditions needs to be true
# or - either one needs to be true
# not - reverse of the condition


a = int(input("Enter the number 1 : "))
b = int(input("Enter the number 2 : "))
c = int(input("Enter the number 3 : "))


if a>b and a>c:
    print("A is greater")
else:
    print("A is lesser")


# Odd or Even

num = int(input("Enter the number : "))

if num%2==0:
    print("Even number")
else:
    print("Odd number")


# Eligible for vote

age = int(input("Enter your age : "))
if age>=18:
    print("Eligible for vote")
else:
    print("Not eligible for vote")


# Eligible for work

if age >=18 and age<=60:
    print("Eligible for work ")
else:
    print("Not Eligible for work")


# Valid Marks

marks = float(input("Enter the marks : "))
if marks>=0 and marks<=100:
    print("Valid Marks")
else:
    print("Not Valid Marks")

#Valid age

if age>0 and age<=110:
    print("Valid age")
else:
    print("Invalid age")

# Gender


gender = input("Enter your gender : ")

if gender == 'm' or gender == 'M':
    print("Male")
else:
    print("Female")



# Vowel or Constants

a = input("Enter the alphabet : ")
if a == 'a' or a == 'e' or a == 'i' or a =='o' or a == 'u':
    print("Vowel")
else:
    print("Constants")


# Exam results
phy = int(input("Enter the phy marks : "))
chem = int(input("Enter the chem marks :"))
maths = int(input("Enter the maths marks : "))
if maths >=45 and phy >= 45 and chem >=45:
    print("Pass")
else:
    print("Fail")



