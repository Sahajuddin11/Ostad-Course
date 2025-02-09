class car:
    def __init__(self,mk,mdl,yr):
        self.make = mk
        self.model = mdl
        self.year = yr
        print(mk,mdl,yr)
    
    def move(self):
        print("this is a red car")
    def horn(self):
        print("hip hip ")
        
mycar = car('toyota','camry',2020) 
mycar.move() 
mycar.horn()   

another_car = car('subaru','forester',2014)
another_car.move() 
another_car.horn()