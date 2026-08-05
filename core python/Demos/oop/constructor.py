## constructor
#1. special / magical method which calls automatically when object of that class is created..
#2. __init__ is the name used as constructor..
#3. you need to specify the parameter at the time of object creating...

class Car:
    def __init__(self, color, brand, price):
        self.color = color
        self.brand = brand
        self.price = price

    def showData(self):
        data=f'COLOR:{self.color}\nBRAND:{self.brand}\nPRICE:{self.price}'
        return data
    
    def start(self):
        print("car started.")

    def stop(self):
        print("car stopped.")

c1 = Car("Toyota","Black", 500000)
print(c1.showData())
c1.start()
c1.stop()