credit_card_no = input("Enter the card number : ")
last_digits = credit_card_no[15:]
four_parts = 'X'*4+' '
display_no = four_parts*3+last_digits
print(display_no)
