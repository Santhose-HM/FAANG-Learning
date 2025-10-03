import uuid
items = [
    ['laptop',1200],
    ['mouse',20],
    ['keyboard',30],
    ['tablet',1400]
]

products = {}

for i in items:
    id = uuid.uuid5(uuid.NAMESPACE_OID,i[0])
    key = id.hex[:6]
    products[key] = i
print(products,"\n")