# Else block
# It will excute if the try block is executed successfully
# Statements which are depend on try block needs to be in else

a,b =10,2
print("Start of the program")
try:
    c =a//b
    print(c)
except (ZeroDivisionError,ValueError,TypeError)as msg:
    print(msg)
else:
    print("Else block Exceuted")

print("End of the Program")