class overloading:
    def add(self,a,b):
        print(a+b)
    def add(self,a,b,c):
        print(a+b+c)
a=overloading()
a.add(10,7,3)
a.add(3,4)