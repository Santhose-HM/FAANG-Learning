# Iteration & Sequences Functions

# sorted(iterable,/,*,key=None,reverse=False)
print(sorted([12,54,200,33,21,4,54,-2],key=abs,reverse=False))

# reversed(seq,/)
print(list(reversed([12,54,200,33,21,4,54,-2])))

# slice(start,stop,step)
l = [12,54,200,33,21,4,54,-2]
new_l = slice(0,8,2)
print(l[new_l])
