# loops
# while loops for loops

# while loop - sentinel loop
# for loop - for each loop



# while <condtion>:
    # statements
# statements


n = int(input("Enter a number : "))

while n>0:
    print(n,end=' ')
    n -=1

print()


# Counter

i = 0
while i<10:
    i=i+1
    print(i,'*',3,'=',i*3)

# Digits of number

num = 2546
while num>0:
    r = num%10
    print(r,end='')
    num = num//10
    

print()
# Count Digits and Sum of Digits

number = int(input("Enter the number : "))
count = 0
sum =0
while number>0:
    r = number%10
    count+=1
    sum+=r
    number//=10
print("The overall count is : ",count)
print("The sum of the digits is: ",sum)



# Reverse a number and Find Palindrome

n = 1221
original = 1221
reverse = 0
while n>0:
    r = n%10
    reverse = (reverse*10)+r
    n//=10
print("The reverse number is : ",reverse)
if original == reverse:
    print("It is Palindrome")
else:
    print("It is not Palindrome")



# Sum of the n numbers

n = int(input("Enter the number : "))
sum = 0
i = 0
while i<=n:
    sum +=i
    i+=1
print("The sum of number is : ",sum)


# Find min and max element

n = 5
print("Enter ",5," Numbers : ")
i = 0
max = float('-inf')
min = float('inf')
while i<n:
    i+=1
    x = int(input(""))
    if x > max :
        max = x
    if x < min:
        min = x
print("The maximum number is : ",max)
print("The minimum number is : ",min)
    
# else suite in while loop




