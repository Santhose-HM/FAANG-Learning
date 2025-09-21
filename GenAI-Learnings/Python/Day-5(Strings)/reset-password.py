new_pass = input("Enter password : ")
confirm_pass = input("Enter confrim password : ")

if new_pass == confirm_pass:
    print('Password Changed')
elif new_pass.casefold()== confirm_pass.casefold():
    print("Check the cases")
else:
    print("Password is not matched")
