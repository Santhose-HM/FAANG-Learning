unit = float(input("Enter the electricity unit : "))
if unit > 0 and unit <=100:
    price = unit*5
    print("The price is : ",price)
elif unit>100 and unit<=200:
    price = (100*5)+(unit-100)*7
    print("The price is : ",price)
else:
    price =(100*5)+(100*10)+(unit-200)*10
    print("The price is : ",price)
