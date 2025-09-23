st = input("Enter a string: ")
st = st.replace(" ","").casefold()
new_st = ''
for s in st:
  if s.isalnum():
    new_st+=s
rev=new_st[::-1]
if rev == new_st:
  print("Palindrome")
else:
  print("Not a Palindrome")