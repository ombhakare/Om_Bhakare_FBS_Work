#Write a program to find the area and perimeter of following figure (Accept the
#length, breadth and radius from user:

length = int(input('enter the length: '))
breadth = int(input('enter the breadth: '))
radius = int(input('enter the radius: '))

area_rect = length * breadth
print(area_rect)

perimeter_rect = 2*(length + breadth)
print(perimeter_rect)

area_cir = 3.14 * radius**2
print(area_cir)

perimeter_cir = 2 * 3.14 * radius
print(perimeter_cir)

half_area_cir = (3.14 * radius**2)/2
half_perimeter_cir = (2 * 3.14 * radius)/2

total_area = area_rect + half_area_cir
total_perimeter = perimeter_rect + half_perimeter_cir

print(f'total area is: {total_area}, total perimeter is: {total_perimeter}')
