# String alignment and Padding (methods)

# ljust(width,fillChar) - left justify
# rjust(width,fillChar) - right justify
# center(width,fillChar) - center
# zfill(width) - zero filling always on left hand side


s = 'Hello'

print("========ljust========")
new_str = s.ljust(7,'*')
print(new_str)
print(len(new_str))
print("========rjust========")
new_str = s.rjust(7,'*')
print(new_str)
print(len(new_str))
print("========center========")
new_str = s.center(7,'*')
print(new_str)
print(len(new_str))
print("========zfill========")
new_str = s.zfill(7,)
print(new_str)
print(len(new_str))


# Strip Methods
# lstrip(chars)- left side chars/spcae optional(if we not give any chars to default remove spaces)
# rstrip(chars) - right side chars/space
# strip(chars) - remove spaces on both sides

print("======lstrip=====")
st = '$Sandy'
print(st)
new_st = st.lstrip('$')
print(new_st)
print("======rstrip=====")
st = 'Sandy!!!'
print(st)
new_st = st.rstrip('!')
print(new_st)
print("======strip=====")
st = '$Sandy$'
print(st)
new_st = st.strip('$')
print(new_st)



# Remove multiple characters using strip

print('========remove multiple chars using strip============')
stt = '#!Hello  $ *'
print(stt)
new_stt = stt.strip('#! $*')
print(new_stt)



