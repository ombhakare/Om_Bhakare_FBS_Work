#3. Write a program to input angles of a triangle and check whether triangle is valid or not.

a1 = int(input("enter the angle 1: "))
a2 = int(input("enter the angle 2: "))
a3 = int(input("enter the angle 3: "))

if(a1+a2+a3 == 180):
    print('the triangle is valid. ')
else:
    print('the triangle is not valid. ')