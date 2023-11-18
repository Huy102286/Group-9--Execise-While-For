import math
total_cost = 0
while True:
    price=input('Enter price:')
    if price=='':
        break
    total_cost += float(price)
print("Total Pennies =",total_cost)

if total_cost % 5  < 2.5:
    print('Total nickles =',math.floor(total_cost))
else: 
    print("Total Nickles = ",math.ceil(total_cost))