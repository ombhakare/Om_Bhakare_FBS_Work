# Calculate the cost of painting the following building’s walls (both interior and
# exterior). You need to accept area (one wall) and cost of both interior and
# exterior wall.



interior = int(input('enter the cost of interior: '))
exterior = int(input('enter the cost of exterior: '))

area_one_wall = 100


i_area= 8 * area_one_wall      #interior area

inter_cost = i_area * interior


e_area = 7 * area_one_wall      #exterior area

exter_cost = e_area * exterior

print(f'interior cost of painting is: {inter_cost}\n exterior cost of painting is: {exter_cost}')


