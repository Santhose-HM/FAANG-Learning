# Python formatted printing

name = 'Raj'
roll = 10
avg = 78.5


print('Name:{0}\nRoll:{1}\nAverage:{2}'.format(name,roll,avg))

# {index:f w.p con}
# index - position of value
# f - flag(:^,:>,:+,:-) alignment
# w - width
# precision - for float values
# conversion - d b x f.....



item = 'Memory Card'
size = 32
price = 11.75


print('{0}GB {1} in ${2}'.format(size,item,price))

data = 100
print('start {0:^15.4f} end'.format(data))

print(f'{size}GB {item:^10} is ${price:.3f}')
