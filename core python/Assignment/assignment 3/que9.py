##9.Input 5 subject marks from user and display grade(eg.First class,Second class ..)


m1 = int(input("enter the marks of subjects 1: "))
m2 = int(input("enter the marks of subjects 2: "))
m3= int(input("enter the marks of subjects 3: "))
m4= int(input("enter the marks of subjects 4: "))
m5= int(input("enter the marks of subjects 5: "))

gain_marks = m1 + m2 + m3 + m4 + m5
total_marks =(gain_marks/500)*100
print(total_marks)

if(total_marks == "90"):
    print("the marks between 90 to 99")

