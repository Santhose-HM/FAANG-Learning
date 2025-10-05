# Caller Class - Like closure function


class Day:
    def __init__(self):
        self.days = {0:'Sun',1:'Mon',2:'Tues',3:'Wed',4:'Thur',5:'Fri',6:'Sat'}
    def __call__(self,dayno):
        return self.days[dayno]
    


d = Day()

print(d(3))