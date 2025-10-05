# Variable Length Positional Arguments

# print() - is the best example of variable length positional-arguments
# writing * before the args take n number of args
# We can have other arguments with variable length arguments but if needs to be before *args
# If we put after the *args it must be keyword only agruments
# Take input of list it take the whole list as tuple like tuple(list)
# If you want to unpack the list and pass then use * before the list

def fun (*args):
   for x in args:
      print(x)


fun(5,10,230,103,47)