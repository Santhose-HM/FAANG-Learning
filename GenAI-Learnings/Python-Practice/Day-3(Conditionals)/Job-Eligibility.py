is_degree = input("Do you have Degree yes/no : ").strip().lower()== 'yes'
experience = int(input("Enter your experience : "))
if is_degree == 'yes' and experience >=2:
    print("You are eligible")
else:
    print("You are not eligible")
