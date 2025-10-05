# Keyword-Only-Arguments
# * This will seperate the arguments after the * all the arguments are keyword others either positional or keyword
# In this we are not allowed to put * at the end


def fun(a,b,*,c,d):
    print(a,b,c,d)

fun(a=5,b=10,c=5,d=20)

# Examples
# fun(5,10,15,20) - Worng
# fun(5,10,c=15,d=20) - Correct
# fun(5,b=10,c=15,d=20) - Correct
# fun(5,10,15,d=20) - Worng