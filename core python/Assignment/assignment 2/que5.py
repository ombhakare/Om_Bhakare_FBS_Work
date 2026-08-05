#5. WAP to calculate selling price of book based on cost price and discount. 

cost_price = int(input("enter the cost price: "))
discount_percent = int(input("enter the dicount: "))

disc_amount = (discount_percent / 100)*cost_price

selling_price = cost_price - disc_amount

print(f' the selling price is: {selling_price}')