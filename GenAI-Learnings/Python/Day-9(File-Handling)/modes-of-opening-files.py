# Modes of file opening

#  r - read a file
# w - wrie a file
# a - apend a file
# r+ - read and write
# w+ - write and read
# a+ - append and write
# x write in a new file only

file = open('Day-9(File-Handling)/MyData.txt','a')
data = 'Hello Welcome Buddy'
file.write(data)
file.close()