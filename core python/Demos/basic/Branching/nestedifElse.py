num = 25
if(num >= 0):
    if(num > 50):
        if(num > 100):
            print(f'{num} is greater than 100 ')
        else:
            print(f'{num} is in the range of 51 - 100')
    else:
        print(f'{num} is in the 0 - 50 category')
else:
    print(f'{num} less than zero')