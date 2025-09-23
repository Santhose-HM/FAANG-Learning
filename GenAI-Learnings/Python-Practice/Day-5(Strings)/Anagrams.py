st1 = input("Enter the string 1 : ")
st2 = input("Enter the string 2 : ")

for s in st1:
    if s.isalpha():
        if st1.count(s)!=st2.count(s):
            print("Not an Angrams")
            break
else:
    print("Anagrams")
