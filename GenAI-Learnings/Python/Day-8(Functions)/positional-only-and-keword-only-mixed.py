# Positional-Only-and-Keyword-Only-Arguments

def fun (a,b,/,c,d,*,e,f):
    print(a,b,c,d,e,f)

fun(10,23,25,d=40,e=12,f=54)

# def fun(a,b,c,/,*,d,e,f) - This is allowed
# def fun(a,b,c,*,/,d,e,f) - This is not allowed


# Examples
# fun(5,10,15,d=20,e=2,f=3) - Correct
# fun(5,,1,15,20,2,f=3) - Worng
# fun(5,10,15,20,e=2,f=3) - Correct
# fun(5,b=10,c=15,f=20) - Worng
