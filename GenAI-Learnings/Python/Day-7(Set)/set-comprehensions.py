# Set Comprehensions
# s = {exp for item in iterable}

s1 = {item for item in range(1,101)}
print(s1)
print(type(s1))

s1 = {item**2 for item in {1,-2,3,-6,-4,5}}
print(s1)

s1 = {x.lower() for x in  'Philipphens'}
print(s1)