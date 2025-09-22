# Special Characters


# [...]  - set of possible characters
# [^...] - all characters expect in bracket
# . - any character expect new line
# ^ - begining of the string
# $ - end of s String
# | - R or S

import re

pattern = '[a-zA-Z0-9]'
st = 'ghfgfguigufASGFDJYY434533636364'
print(re.match(pattern,st))
print(re.fullmatch(pattern,st))


# [a-z]+ all lower case words
# [A-Z]+ all upper case words
# [A-Z][a-z]* all dictionary words
# [^a-z]+ exclude all lower case words
# .+  any character with any case will include except newline
# \.+ just dot itself any times
# ^http.+ must match only starts with http and after anything
# com$ ending with com
# com|org must match with com/org

pattern = '[A-Z][a-z]+ [A-Z][a-z]+'
st = 'Sam Cs'
print(re.fullmatch(pattern,st))
