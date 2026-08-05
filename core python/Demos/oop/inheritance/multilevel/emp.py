from person import Person

class Emp(Person):
    def __init__(self, nm, age, id, sal):
        super().__init__(nm, age)
        self.eid = id
        self.sal = sal

    def display(self):
        return super().display()+f'\nEID:{self.eid}\nSALARY:{self.sal}'

e1 = Emp('om', 22, 24455, 50000)
print(e1.display())