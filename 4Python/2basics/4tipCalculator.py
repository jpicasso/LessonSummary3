check = float(input('how much is the meal?'))
tax_rate = 0.08
tip_rate = input ('how much do you want tip?')

tax = check * tax_rate
tip = check * tip_rate
total = check + tax + tip

print('the total is ${}.' .format(total))