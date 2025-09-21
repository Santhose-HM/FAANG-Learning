# Case Conversions

# capitalize() - Only First Letter is capital
# upper() - Convert to all in uppercase
# lower() - Convert all into lower
# title() - Make every word first letter capital()
# swapcase() - Inverse upper to lower/ lower to upper
# casefold() - same as lower,but this works for all langugae perfectly


s1 = 'hello dear'
print(s1)

# capitalize()
new_s1 = s1.capitalize()
print(new_s1)

# upper()
new_s2 = s1.upper()
print(new_s2)

# lower()
new_s3 = s1.lower()
print(new_s3)

# title()
new_s4 = s1.title()
print(new_s4)


# swapcase()
s2 = 'HeLlO dEaR'
new_s5 = s2.swapcase()
print(new_s5)


# casefold
s3 = 'HELLO DEAR'
s4 = 'Hola, mi amor'
new_s6 = s3.casefold()
new_s7 = s4.casefold()
print(new_s6)
print(new_s7)

