# Regular Expressions


# To define  Pattern Matching
# Quantifiers
# Special Characters
# Escape Sequences


# Pattern
# re - to use class, functions which are related to re(regular expression) we need to import it

# Three ways to use import a module

# import re
# import re as regex
# from re import *


import re

# compile(pattern,flag = 0) - compiling regex
# validation
# match(pattern,string,flag = 0)- check only begining
# fullmatch(pattern,string,flag=0) - fully check
# Search and Extract
# search(pattern,string,flag=0)
# findall(pattern,string,flag=0)
# split(pattern,string,maxslip = 0, flag = 0)

print(re.match('abc','abcdef'))
print(re.fullmatch('python','py'))
print(re.fullmatch('python','python').group())
print(re.search('very','python is very easy').span())
print(re.findall('can','can you can a can as a cancer'))





