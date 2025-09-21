input_str1 = input("Enter the string one : ")
input_str2 = input("Enter the string two : ")


s1 = input_str1.lower()
s2 = input_str2.lower()

for x in s1:
    if x.isalpha():
        if s1.count(x)!=s2.count(x):
            print('not anagrams')
            break
else:
    print('Anagrams')
