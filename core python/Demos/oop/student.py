class Student:
    count = 0
    def __init__(self, roll_no, name,age):
        Student.count += 1
        self.roll = roll_no
        self.name = name
        self.age = age
    
    def displayData(self):
        print("roll no:", self.roll)
        print("name:", self.name)
        print("age:", self.age)
        
        
    #@staticmethod......................it is a static method used when the s1.totalStudent() is mention
    def totalStudent():
        print("Total students:", Student.count)

s1 = Student(101,"om",22)
s1.displayData()


s2 = Student(102,"ravi",23)
s2.displayData()

Student.totalStudent()
#s1.totalStudent().............................