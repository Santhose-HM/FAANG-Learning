sentence = input("Enter a sentence : ")
sen_list = sentence.split()
bigger = ''
for s in sen_list:
    if len(s)> len(bigger):
        bigger = s
print(f"The larger word is {bigger}")
