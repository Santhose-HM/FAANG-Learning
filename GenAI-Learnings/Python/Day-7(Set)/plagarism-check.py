import re
str1 = ('Time is the most valuable thing we have if we lost once it never returns')
str2 = ("We never get back the time once it's" "gone-it's truly the most valuable resource")

words1 = re.findall(r'\w+',str1.lower())
words2 = re.findall(r'\w+',str2.lower())
w_set1 = set(words1)
w_set2 = set(words2)

common = w_set1 & w_set2
unique = w_set1 | w_set2
ratio = len(common) / len(unique)
print("Jacard Similarity is : ",ratio)
