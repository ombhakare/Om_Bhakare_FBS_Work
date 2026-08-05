#8.Write a program to swap two numbers using third variable.??

x = 10 
y = 20 
z = x + y

print(f'before swapping x : {x}, y:{y} . ')
y = z - y
print(y)

x = z - x
print(x)

print(f'after swapping x is: {x}, y is : {y}. ')