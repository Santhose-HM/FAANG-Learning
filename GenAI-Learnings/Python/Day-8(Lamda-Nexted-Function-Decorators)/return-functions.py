# Returning Functions

def Outer():
    def Inner():
        print('Welcome')
    return Inner


f = Outer()
print(f)