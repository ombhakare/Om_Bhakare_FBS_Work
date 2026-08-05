class Emp:
    def __init__(self, id, name, sal, dept):
        self.id = id
        self.name = name
        self.sal = sal
        self.dept = dept

    def __str__(self):
        return f'{self.id}, {self.name}, {self.sal}, {self.dept}, '

e1 = Emp(1012, "om", 20000, "data analyst")
print(e1)