#4.Write a program to enter P, T, R and calculate simple Interest.??

p = int(input('enter the value: '))
r = int(input('enter the value: '))
t = int(input('enter the value: '))

s_i = p * r * t / 100

print(f'simple interest is : {s_i}')