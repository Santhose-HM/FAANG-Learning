# Quantifiers


# + - 1 or more time repition(min one time)
# * - 0 or more time
# ? - 0 or 1
# {m} excatly m/n times
# {m,n} from m to n (minimum is m maximum is n)

import re
pattern = 'a+'
st = 'aaaaaaaa'
print(re.match(pattern,st))
pattern = '(ab)+'
st = 'ababab'
print(re.fullmatch(pattern,st))
pattern = '[abc]+'
st = 'abcd'
print(re.match(pattern,st))
pattern = 'a*'
st = 'b'
print(re.match(pattern,st))
pattern = '(avavav)*'
st = 'sfgd'
print(re.fullmatch(pattern,st))
pattern = '(abc)?'
st = 'abd'
print(re.match(pattern,st))
print(re.fullmatch(pattern,st))
pattern = '[eimt]{4}'
st = 'time'
print(re.match(pattern,st))

