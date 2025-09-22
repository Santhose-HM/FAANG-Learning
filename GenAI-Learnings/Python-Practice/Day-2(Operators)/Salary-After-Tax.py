original_salary = int(input("Enter the salary amount : "))
if original_salary > 50000:
    tax = 0.20*original_salary
    print("The tax amount is : ",tax)
    home_take_salary = original_salary-tax
    print("The home take salary is : ",home_take_salary)
else:
    tax = 0.10*original_salary
    print("The tax amount is : ",tax)
    home_take_salary = original_salary-tax
    print("The home take salary is : ",home_take_salary)

    
