# Positional-Only-Arguments
# / is used to seperate  postional only and keyword only
# def fun (a,b,/c,d)
# In this the first part is always positional and second part either positional or keyword
# We can adjust the / based on number of arguments needs to positional if it is end all of them are positional
# def fun(a,b,c,d,/) - It means everything is positional
# def fun(/,a,b,c,d) - It is not allowed atleast one argument before the /

def fun(a,b,/,c,d):
    print(a,b,c,d)


fun(5,10,c=15,d=20)

# Examples 
# fun(a=5,b=10,c=15,d=20) - Worng
# fun(5,10,c=15,d=20) - Correct
# fun(5,10,15,d=20) - Correct
# fun(5,10,15,20) - Correct
# fun(a=5,b=10,c=15,d=20) - Worng
