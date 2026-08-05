class Person:
    def setData(self, nm, a, add):
        self.name = nm
        self.age = a
        self.add = add
    
    def displayData(self):
        print("NAME:", self.name)
        print("AGE:", self.age)
        print("ADDRESS:", self.add)
        print("###########################")

p1 = Person()
p1.setData("sachin", 57, "pune")
p1.displayData()

p2 = Person()
p2.setData("jai" , 22, "kolhapur")
p2.displayData()