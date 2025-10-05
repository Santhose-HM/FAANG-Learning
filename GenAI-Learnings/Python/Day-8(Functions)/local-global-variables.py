# Local and Global Variables
# The variable which is declared inside function/block of code is local variable and outside is called global variable
# If you change value of global variable inside a block of code  it will only work on the block of code not throught the program
# Suppose if you want to change mention 'global' 
# When you declare the variable we need to delcare global variable above the function call
# locals() - prints all the local variable in form of dictionary
# globals() - prints all the global variable in form of dictionary along with predefined globals in the program


g = 5.25
print('Outside-1:',g)
def fun():
    global g
    a =10
    g= 199
    print('local :',a)
    print('global:',g)


fun()
print('Outside-2:',g)



