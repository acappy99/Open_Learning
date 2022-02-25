# Present value of perpetuity

print('')
print('Present value of a perpetuity')
print('')
perp = float(input('Enter the cash flow that pays into perpetuity: '))
print('')
r = float(input('Enter the required rate: '))
print('')
print('')
g = (input('Enter the growth rate (or leave blank): '))
print('')
if g == '':
    g = 0
g = float(g)

value = perp/(r-g)
print('The value of the perpetual cash flows is:',value)
print('')