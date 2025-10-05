# Finally Block
# This only usefull inside the function


def fun():
    try:
        x = int('abc')
        return x
    except Exception as msg:
        raise msg
    finally:
        print("End of the function")

try:
    print(fun())
except Exception as e:
    print(e)
