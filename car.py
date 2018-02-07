class Car(object):
    def __init__(price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 10000:
            self.tax = 15
        else:
            self.tax = 12
car1 = Car(2000,"35mph","full","15mpg")
