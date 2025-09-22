bill_amt = int(input("Enter the bill amount : "))
no_frnds = int(input("Enter the no.of frnds : "))
tax = 0.10 * bill_amt
print("The tax amount is : ",tax)
tip = 0.05 * bill_amt
print("The tip amount is : ",tip)
detuction = bill_amt + tax + tip
print("The detuction amount is : ",detuction)
split_amt = detuction/no_frnds
print("The split amount is : ",split_amt)

