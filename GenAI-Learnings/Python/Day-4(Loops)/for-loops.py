# for loops/ for Each loops
# range()
# parameters taken by the range fn -> start,stop,step
# start is optional, stop is mandatory, step is optional
# default start value is 0 and default step value is 1
# It will stop before the last value
# Example range(5) then it is from 0,1,2,3,4
# range(1,5) then it gives 1,2,3,4
# range(6,11)  then 6,7,8,9,10
# range(0,10,2)  then 0,2,4,6,8
# We can use negative value also
# range(-5,-1) then -5,-4,-3,-2,-1
# range(-2,3) then -2,-1,0,1,2
# range(10,5,-1) then 10,9,8,7,6 so if you want to go backward use -ve values
# The range will give the values one by one in for loop an at once

# Syntax
# for var in sequence:
    # Statement1
    # Statement 2

# Working with integers

for i in range(5):
    print(i)


# Working with string

str1 = "Python"

for x in str1:
    print(x,end=",")



# Sum of the n Natural Numbers
print()
num = int(input("Enter the range : "))
sum = 0
for n in range(1,num+1):
    sum+=n
print("The sum of",num,"is",sum)


# Factorial of the N Numbers

fact = 1
for f in range(1,num+1):
    fact*=f
print("The factorial of",num,"is",fact)


# Fibonacci Series
# for i = 2 term_one = 0, term = 1, term_three = 0+1 =1
# term_one = term_ two -> term_one = 1
#term_two = term_three -> term_two = 1
# i = 3
# term_three = 2
# term_one = 1
# term_two = 2
# i = 4
# term_three = 3
# term_one = 2
# term_two = 3
# i = 5
# term_three = 5
# term_one = 3
# term_two = 5
# i = 6
# term_three = 8
# term_one = 5
# term_two = 8
# i = 7
# term_three = 13
# term_one = 8
# term_two = 13
# i = 8
# term_three = 21
# term_one = 13
# term_two = 21
# i = 9
# term_three = 34
# term_one = 21
# term_two = 34
# Loop ends because the range is upto 10 so only upto 9 will run from 2 to 9
term_one = 0
term_two = 1
print(term_one)
print(term_two)
term_three = 0
for i in range(2,num):
    term_three = term_one+term_two
    print(term_three)
    term_one = term_two
    term_two = term_three
print("The term_one is : ",term_one)
print("The term_two is : ",term_two)
print("The term_three is : ",term_three)



# Prime Numbers and Factors of the numbers
# Any number which divides a numbers that give remainder zero it is factors
# If you take n = 15 then factors are 1,3,5,15
# So factors of 15 are 1,3,5,15
# n = 12
# Factors of 12 are 1,2,3,4,6,12

for factor in range(1,num+1):
    if num%factor == 0:
        print(factor,end=",")


# Prime Number
# If a number is not exactly divisible by others more than 1 and itself
print()
number = int(input("Enter the number : "))
count = 0
for prime in range(1,number+1):
    if number%prime == 0:
        count+=1
if count == 2:
    print("The given number",number,"is prime")
else:
    print("The given number",number,"is not prime")
        

# break continue,pass,else-suite

# break - It will stop the loops when it hits the break
# continue - It will skip the particular iteration and executes
# pass - If I don't want to do anything then use pass

# Break
print("Break")
for i in range(1,4):
    if i%2 == 0:
        break
    print(i)
# Continue
print("Continue")
for i in range(1,4):
    if i%2 == 0:
        continue
    print(i)
# Pass
print("Pass")
for i in range(1,4):
    if i%2 == 0:
        pass
    print(i)
# Else Suite
print("Else Suite")
for i in range(1,4):
    print(i)
else:
    print("Else part of loop")
