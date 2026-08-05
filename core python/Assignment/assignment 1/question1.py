#1. WAP to calculate the percentage of student based on marks of any 5 subjects.??

m1 = int(input('enter the marks of 1 : '))
m2 = int(input('enter the marks of 2 : '))
m3 = int(input('enter the marks of 3 : '))
m4 = int(input('enter the marks of 4 : '))
m5 = int(input('enter the marks of 5 : '))

gain_marks = m1 + m2 + m3 + m4 + m5

perc = (gain_marks/500)*100

print(f'percentage is : {perc}')