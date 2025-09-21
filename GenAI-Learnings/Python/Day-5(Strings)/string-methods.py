# String Methods
# Find and Index(rfind and rindex)
# count()


# find(sub,start,end)
# stubstring start index, end index

s = 'Hello How are you ?'

# find - It refers the first occurance
print('============find()=========')
print(s.find('o'))
print(s.find('How'))
print(s.find('k'))
print(s.find('o',6))
print(s.find('o',5,7))


#rfind()- It refers the last occurance
print('============rfind()=========')
print(s.rfind('o'))
print(s.rfind('o',0,15))
print(s.rfind('o',0,7))
print(s.rfind('kite'))

# index()
print('============index()=========')
print(s.index('How'))


# rindex()
print('============rindex()=========')
print(s.rindex('o'))


# count()

print('============count()=========')
print(s.count('H'))
