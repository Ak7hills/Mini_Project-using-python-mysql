class vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage
    def seating_capacity(self,capacity):
        return(f"The seating capacity of a {self.name} is {capacity} passengers")
    def charge(self,capacity):
        charge=capacity*100
        return charge
class bus(vehicle):
    def amount(self):
        t1=vehicle.charge(self,50)
        total=t1+((10*t1)/100)
        print("total amount is",total)
A=bus("xxx",100,50)
A.amount()

class vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage
    def seating_capacity(self,capacity):
        return(f"The seating capacity of a {self.name} is {capacity} passengers")
class bus(vehicle):
    def seat(self):
        print(f"The seating capacity of a {self.name} is {capacity} passengers")
a=bus("bus",100,50)
print(a.seating_capacity(50))