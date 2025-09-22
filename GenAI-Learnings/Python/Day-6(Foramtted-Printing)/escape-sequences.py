# Escape Sequences

# \n - new line
# \r - carriage return(move cursor in the begining of the new line)
# \f - line feed
# \t - tab
# \v - vertical tab
# \b - backspace
# \a - alert
# \  - ignore new line
# \\ - back slash
# \' - quote
# \" - double quote
# \o - octal
# \x - hexa-decimal
# \xhh - 2 digit hexa
# \uxxxx - 4 digit hexa
# \Uxxxxxxxx - 8 digit hexa
# \N{name} - name in Unicode Database

print('Hello\nWorld')
print('Valid\rSo')
print('Step1\fStep2')
print('Hello\tWorld')
print('Hello\v World')
print('Hello\b')
print('Completed\a')
print('Line1\
Line2')
# print('C:\') - It gives error
print('C:\\')
print('Ajay\'s')
print('\"Important\"')
print('\101') # mmust give 3 digits
print('\x41') # must put the x in the begining 2 digit hexa
print('\u0041') #4 digit hexa
print('\U00000041') # 8 digit hexa
print('\N{grinning face}')
print('\N{rupee sign}')
