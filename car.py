class Car(object):
    def __init__(self,price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 10000:
            self.tax = 15
        else:
            self.tax = 12
    def disply_all(self):
        print self.price
        print self.speed
        print self.fuel
        print self.mileage
        print self.tax
        return self

car1 = Car(2000,"35mph","full","15mpg")
car2 = Car(2000,"5mph","not full","105mpg")
car3 = Car(2000,"15mph","kind of full","95mpg")
car4 = Car(2000,"25mph","full","25mpg")
car5 = Car(2000,"45mph","empty","25mpg")
car6 = Car(200000,"35mph","empty","15mpg")
car1.disply_all()