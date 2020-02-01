headphone_price = 75.00
latop_price = 2000.00


lQuantity = input('How many laptops do you want?')
lQuantity = int(lQuantity)

hQuantity = input('How many headphones do you want?')
hQuantity = int(hQuantity)

total = hQuantity*headphone_price+lQuantity*latop_price

print('Your total is ${}' .format(total))