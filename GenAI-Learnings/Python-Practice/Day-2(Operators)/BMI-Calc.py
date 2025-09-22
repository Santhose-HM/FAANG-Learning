weight = float(input("Enter the weight : "))
height = float(input("Enter the height : "))

bmi = weight/(height **2)
if bmi<18.5:
    print("Thin")
elif 18.5<= bmi<25:
    print("Normal")
elif 25<= bmi < 30:
    print("Over Weight")
else:
    print("Obse")

