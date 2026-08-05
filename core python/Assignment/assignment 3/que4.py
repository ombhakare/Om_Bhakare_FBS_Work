#4. Write a program to input all sides of a triangle and check whether triangle is valid or 
#not. 

side1 = int(input("enter the side of triangle: "))
side2 = int(input("enter the side of triangle: "))
side3 = int(input("enter the side of trianglr: "))

if(side1 + side2 > side3):
    if(side2 + side3 > side1):
        if(side3 + side1 > side2):
            print('it is a valid triangle')
        else:
            print('it is not a valid triangle')
    else:
        print('it is not valid triangle')
else:
    print('it is not a valid triangle')



    