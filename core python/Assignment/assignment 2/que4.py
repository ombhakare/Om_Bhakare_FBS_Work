#4. WAP to calculate area of triangle and rectangle ??

base = int(input("enter the base of triangle: ")) 
height = int(input("enter the height of triangle: "))

length = int(input("enter the length of rectangle: "))
breadth = int(input("enter the breadth of rectangle: ")) #...........take as input by user

area_tri = 1/2 * (base * height)                    #formula of triangle
print(f'area of triangle is: {area_tri}')

area_recta = length * breadth                       #formula of rectangle
print(f'area of rectangle is: {area_recta}')