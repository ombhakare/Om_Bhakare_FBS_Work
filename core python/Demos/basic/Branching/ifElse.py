#branching (if)
var1 = False
if(var1):
    print("this if block is executed. ")

print('program executed successfully.')

var1 = True  
if(var1):
    print("this block is executed ")

print("program is executed successfully. ")

#example Q2.
num = int(input('enter the number: '))
if(num % 2==0):
    print(f'{num} is an even number. ')

print('end of program. ')

# example 3.
var1 = int(input('enter the number:'))
if(var1 % 2 == 0):
    print(f'{var1} is an even number.')
else:
    print(f'{var1} is an odd number.')