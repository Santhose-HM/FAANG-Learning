# String joining and spliting


# replace(old,new,count) - replace old with new(count is optional)
# join(iterable) - it will add the character between them
# split(sep,maxsplit) - default remove spaces
# rsplit(sep,maxsplit) - works from right hand side
# splitlines(keepends) - split line wise

# If we give the char/string which is not availabe it wil give the copy of the same string
print('======replace========')
st = 'a-b-c-d-e'
print(st)
new_st = st.replace('-','*')
print(new_st)
new_st1 = st.replace('-','*',1)
print(new_st1)


print('=====join=======')
stt = 'xyz'
stt2 = 'abc'
new_stt = stt.join(stt2)
print(new_stt)
st1 = './'
st2 = 'abc'
new_st1 = st1.join(st2)
print(new_st1)


print('=====split=======')
s1 = 'John,Smith,Ajay'
print(s1)
s2 = s1.split() # It gives list
print(s2)
s3 = s1.split('h') #It will split with h means remove h 
print(s3)
s4 = s1.split(',',1)
print(s4)
print(type(s4))

print('=====rsplit=======')
s1 = 'John,Smith,Ajay'
print(s1)
s2 = s1.rsplit(',',1) # It gives list
print(s2)


print('=====splitlines=======')
s1 = 'Loremeihuierhioiuhiuewfuiruguycbuyrfer.\niuerewugwyrybfyi.\n'
print(s1)
s2 = s1.splitlines('.')
