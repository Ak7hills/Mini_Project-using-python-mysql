class circle:
    def __init__(self,r):
        self.r=r
    def area(self):
            print(self.r**2*3.14)
a=circle(3)
a.area()