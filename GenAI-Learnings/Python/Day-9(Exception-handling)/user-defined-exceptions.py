# User Defined Exceptions


class NegativeDimensionError (Exception):
    def __init__(self):
        self.msg = 'Negative Dimension'
    
    def __str__(self):
        return self.msg




def area(length,breadth):
    if length>=0 and breadth>=0:
        a = length*breadth
        return a
    else:
        raise NegativeDimensionError()

res = 0
try:
    res = area(10,-4)
except Exception as msg:
    print(msg)
else:
    print(res)
finally:
    print("Program Ended")