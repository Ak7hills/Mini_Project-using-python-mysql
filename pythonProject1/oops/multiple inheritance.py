#calculator
class calcu1:
    def sum(self,a,b):
        return a+b
class calcu2:
    def sub(self,a,b):
        return a-b

    def mul(self,a,b):
        return a*b
class derived(calcu1,calcu2):
    def div(self,a,b):
        return a/b

d=derived()
print(d.div(6,3))
print(d.mul(6,3))
print(d.sub(6,3))
print(d.sum(6,3))
