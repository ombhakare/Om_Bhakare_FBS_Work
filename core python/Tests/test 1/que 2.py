# Write a program to calculate simple interest based on Principal, Rate and Time
# (SI = P*R*T/100) 
principle = int(input('enter the principle: '))
rate = int(input('enter the rate: '))
time = int(input('enter the time: '))

s_i = (principle * rate * time)/100

print(f'simple interest is: {s_i}')