class Shape:
    def __init__(self, id , area):
        self.id = id
        self.area = area

    def display(self):
        print("ID:", self.id)
        print("area:", self.area)

class Rectangle(Shape):
        def __init__(self, id , area, l, b):
            super().__init__(id,area)
            self.length = l
            self.breadth = b

        def display(self):
            super().display()
            print("LENGTH:", self.length)
            print("breadth:", self.breadth)

r1 = Rectangle("rect", 800, 40, 20)
r1.display()



    