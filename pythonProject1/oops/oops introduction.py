# class is a collection of objects
# object is a blueprint of class
#     features:
#     *object
#     *class
#     *polymorphism
#     *abstraction
#     *encapsulation
#     *inheritance

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def test(self):
        print("Hi, my name is ",self.name,"my age is ",self.age)
A=Person("Akhil",22)
A.test()

class car:
    def __init__(self,modelname,year):
        self.modelname=modelname
        self.year=year
    def display(self):
        print(self.modelname,self.year)
c1=car("BMW",2019)
c1.display()

class A:
    i=123
    def __init__(self):
        self.i=12345
print (A.i)
print (A().i)