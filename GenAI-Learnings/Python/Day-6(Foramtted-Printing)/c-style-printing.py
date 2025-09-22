# C style Priniting

item = 'Memory Card'
size = 32
price = 11.75

# In general we print like this 
print('Cost of',size,'GB',item,'is $',price)


# Now we can print this with C style printing

# %d - decimal
# %i - integer
# %o - octal
# %x - hexa
# %f - float
# %F - float
# %g - General Float
# %e - Scientific
# %E - Exponent
# %s - string


print('Cost of %dGB %s is $%2.2f'%(size,item,price))
