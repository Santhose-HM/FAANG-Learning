# Print functions
# Seperator
# End of Line

# print(object,sep = '',end='\n') - default sep is white space, default end will be new line
print('hi',12,32.24,sep=',')
print('Hello',end='')
print('World')

# Overall signature of print()
# print(object,sep='',end='\n',file=sys.stdout,flush = False)

# object - content needs to print
# seperator - which seperates the multiple objects while prin
# end  - end of line either we want new line at the en after print/not
# file - which way our out print needs to be print
# flush - force push the buffer into the display to print
