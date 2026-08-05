# 11. Write a program to accept an integer amount from user and tell minimum 
# number of notes needed for representing that amount. 

amount = int(input('enter the amount: '))

mini_notes1 = amount // 2000

mini_notes2 = amount % 2000


mini_notes3 = mini_notes2 // 1000

mini_notes4 = mini_notes2 % 1000


mini_notes5 = mini_notes3 // 500

print(f'minimum notes of is : {mini_notes1},{mini_notes3},{mini_notes4}. ')