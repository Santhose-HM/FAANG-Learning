# Escape Sequences

# \d - digits(0-9)
# \D - non-digits(a-z,A-z and special characters)
# \w - alphaNumberic(a-zA-Z0-9)
#\ W - special characters
# \s - White Space
# \S - Non white space
# \A - Starting of a string
# \Z - End of the string

import re

#import re

# date-pattern
pattern = r'\d{2}/\d{2}/\d{4}'
st = '12/03/2023'
print(re.fullmatch(pattern, st))

# password (at least 8 characters, any type)
pattern = r'[\w\W]{8,}'
st = 'Password@123'
print(re.fullmatch(pattern, st))

# email id (basic version)
pattern = r'\w+\.?\w+@gmail\.com\Z'
st = 'sam@gmail.com'
print(re.fullmatch(pattern, st))
