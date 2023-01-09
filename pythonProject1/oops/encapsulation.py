class student:
    def __init__(self,name,age):
        self.name=name
        self._age=age
    def bio(self):
        print("hlo,my name is ",self.name,"my age is",self._age)
A=student("Akhil",22)
A.bio()
