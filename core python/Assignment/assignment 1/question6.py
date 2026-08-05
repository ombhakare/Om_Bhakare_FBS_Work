#6.WAP to input two angles from user and find third angle of the triangle.??

ang1 = int(input('enter the angle 1: '))
ang2 = int(input('enter the angle 2: '))

sum = ang1 + ang2

third_ang = 180 - sum

print(f'the third angle is:{third_ang}')