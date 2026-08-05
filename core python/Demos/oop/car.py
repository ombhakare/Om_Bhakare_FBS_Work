class Car:
    def setData(self, color, brand, price):
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

c1 = Car()
c1.setData("Toyota","Black", 500000)
print(c1.showData())
c1.start()
c1.stop()