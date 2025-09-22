speed = int(input("Enter the speed : "))
if speed >80:
    extra_speed = speed-80
    fine = 500 + (10*extra_speed)
    print("Fine amount is : ",fine)
elif speed < 40:
    print("Warning : Driving too slow")
else:
    print("Safe")
