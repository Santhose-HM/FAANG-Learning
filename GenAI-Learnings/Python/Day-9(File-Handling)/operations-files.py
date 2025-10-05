# Opeations of files

# read - read(size), readline(), readlines()
# write - write(str), writelines(str), truncate()
# readble(), writeable(), close()
# tell(), seek(offest,2)

with open('data.txt','r') as file : # automatically close the file 
    data = file.read()
    print(data)