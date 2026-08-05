num = 668

d1 = num % 10
print(d1)

num = num // 10
print(num)          #.......

d2 = num % 10
print(d2)

num = num // 10
print(num)         #..........

d3 = num % 10
print(d3)

num = num // 10
print(num)         #..........

print(f'd1:{d1}, d2:{d2}, d3:{d3} ')

print(f'sum of digit id { d1 + d2 + d3}')