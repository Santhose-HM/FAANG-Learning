menu =[]
for i in range(1,5):
    item_name = input("Enter the item name : ")
    price = input("Enter the price value : ")
    dash = 20 - len(item_name) - len(item_name)
    menu.append(item_name+('-'*dash)+price)

for i in menu:
    print(i)
