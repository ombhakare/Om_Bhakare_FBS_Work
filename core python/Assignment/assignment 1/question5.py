#Q5.Write a program to enter P, T, R and calculate Compound Interest.??

p = int(input('enter the value: '))
r = int(input('enter the value: '))
t = int(input('enter the value: '))

c_i = p * (1+r/100)**3-p

print(f'compound interest is ; {c_i}')