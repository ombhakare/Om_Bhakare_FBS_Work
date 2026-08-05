#1. Write a program to check if the given number is positive or negative.


num = float(input("enter the number: "))

if(num == 0):
    print('it is a neutral number')

elif(num > 0 ):
    print('it is a positive number')
    
else:
    print('it is a negative number')