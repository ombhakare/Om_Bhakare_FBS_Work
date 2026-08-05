class Car:
    def __init__(self, color='white', brand='toyota', price=500000):
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

print("########")

c2 = Car()
print(c2.showDAta)
c2.start()
c2.stop()