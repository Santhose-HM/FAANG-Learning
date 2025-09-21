# Strings
# Collection of character enclosed with a ''
# It can contains any character/letters from the keyboard
# It has index value from 0 to n as like all language
# Also it has negative index from -1 to n


str1 = "Hello"
print("This one is reterive via positve index : ",str1[0])
print("This one is reterive via negative index : ",str1[-5])


# Length of the string
# To find a length we need to count the total letters

print("Length of the string : ",len(str1))


# Traversing a string

for st in str1:
    print("Each of the string is : ",str1)
    
# Traversing the string using indexes

for st in range(len(str1)):
    print("Each element of string using indexes : ",str1[st])

# String Literals

s1 = 'Hello'
s2 = "Hello"
s3 = ''' Hello '''
# Using 3 double quotes we can write multi line
s4 = """ Hello """
# How to use opostipe 's
s5 = "Clark's"


