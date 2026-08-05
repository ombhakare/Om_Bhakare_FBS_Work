num = int(input("enter the number: "))

temp = num
while(temp > 0):
    d = temp % 10
    print(d)
    temp = temp // 10