from emp import Emp

class SoftDev(Emp):
    def __init__(self, nm, a, id, sal, tech ):
        super().__init__(nm, a, id,sal)
        self.tech = tech

    def display(self):
        return super().display()+f'\nTECH:{self.tech}'

sd = SoftDev('om',22,344,2345,"python")
print(sd.display())




