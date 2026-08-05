num = int(input("enter the prime number: "))
for i in range(2,num):
    if(num % 2 == 0):
        print(f'{num} is not a prime number')
        break
else:
    print(f'{num} is a prime number')