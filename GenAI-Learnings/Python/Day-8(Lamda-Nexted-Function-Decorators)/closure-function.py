# Closure Function
# It has  nested function, returning function, Inner Function Access Outer Varibles

def Outer():
    msg = 'Welcome'
    def Inner():
        print('+'*10)
        print(msg)
        print('+'*10)
    return Inner()

f = Outer()

f

