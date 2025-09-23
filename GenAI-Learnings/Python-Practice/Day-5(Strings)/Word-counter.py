paragraph = input("Enter a paragraph : ")
print(paragraph)
para = paragraph.lower().split()
unique = set()
p = []
for word in para:
    if word not in unique:
        p.append(word)
        unique.add(word)
for i in p:
    times = paragraph.count(i)
    print("The word {} is in {} times".format(i.upper(),times))
    
