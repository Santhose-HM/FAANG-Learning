input_Str = input("Enter the string : ")
clean_Str = ''

for i in input_Str:
    if i.isalpha() or i.isspace():
        clean_Str+=i
    else:
        clean_Str = clean_Str+' '
print(clean_Str)
