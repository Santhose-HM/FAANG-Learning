count = 0
while True:
    pin = int(input("Enter your pin : "))
    authorize_pin = 2342
    if pin == authorize_pin :
        print("Allow Withdrawl")
        break
    else:
        count +=1 
        print(count)
        if count == 3:
          print("Account is locked")
          break
        else:
            print("Try again")
