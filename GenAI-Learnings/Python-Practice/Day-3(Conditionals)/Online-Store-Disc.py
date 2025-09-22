purchase_amt = int(input("Enter the purchase amount : "))
if purchase_amt > 10000:
    print("You have 20% discount")
    discount_amt = purchase_amt - (purchase_amt*0.20)
    print("The amount need to pay is ",discount_amt)
elif purchase_amt > 5000:
    print("You have 10% discount")
    discount_amt = purchase_amt - (purchase_amt*0.10)
    print("The amount need to pay is ",discount_amt)
else:
    print("No Discount")
    print("The amount need to pay is ",purchase_amt)
