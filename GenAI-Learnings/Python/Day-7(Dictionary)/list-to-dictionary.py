header  = ['name','age','city']
data = [
    ['James',25,'NY'],
    ['Smith',24,'PAR'],
    ['Kiran',30,'DEL'],
    ['Raj',27,'DEL']
]


result = []
length = len(header)
for i in range(length):
    newdict = {}
    for row in data:
        if row[i] not in newdict:
            newdict[row[i]] = row
        else:
            newdict[row[i]].append(row)
    result.append(newdict)

for i in range(length):
    print("\n"+header[i])
    for key,value in result[i].items():
        print(f"{key:<10}:{value}")