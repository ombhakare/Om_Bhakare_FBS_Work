class Employee:
    def __init__(self, id, nm, sal, dept):
        self.eid = id
        self.ename = nm
        self.salary = sal
        self.dept = dept

    def displayData(self):
        return f'ID:{self.eid}\nNAME:{self.ename}\nSALARY:{self.salary}\nDEPARTMENT:{self.dept}'

    def __del__(self):
        print("destructor is called.")

e1 =Employee(101, "om", 40000, "python developer")
print(e1.displayData())
print("##################")

e2 = Employee(102,"aman",60000,"data analyst")
print(e2.displayData())
print("########################")