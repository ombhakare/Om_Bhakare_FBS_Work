#Q7. Program to Find the Roots of a Quadratic Equation.??

a = int(input('enter the value: '))
b = int(input('enter the value: '))
c = int(input('enter the value: '))

sqrt = ((b**2)- (4*a*c))**0.5

res1 = (-b-sqrt)/2*a

res2 = (-b+sqrt)/2*a

print(f'sqrt is: {sqrt}, res1 is: {res1}, res2 is {res2}. ')

