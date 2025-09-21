# Match Case
# It's just a switch case like in other languages without break and default(instead of use case_)

# Day of a Week


day_no = int(input("Enter the day number : "))

match day_no:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thrusday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _ :
        print("Invalid choice")
    
