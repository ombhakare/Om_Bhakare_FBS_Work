##5. Write a program to check whether the triangle is equilateral, isosceles or scalene 
#triangle.

side1 = int(input("enter the side 1: "))
side2 = int(input("enter the side 2: "))
side3 = int(input("enter the sdie 3: "))

if(side1 == side2 == side3):
    print("this is the equilateral triangle ")
elif(side1 == side2 != side3 or side2 == side3 != side1 or side3 == side1 != side2):
     print("it is isoscales triangle")
elif(side1 != side2 != side3):
    print("this is scalen triangle")
    
