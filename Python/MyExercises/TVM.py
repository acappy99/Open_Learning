# Time value of money

# PV of Cash Flows Calculator

print('')
print('Present value of cash flows')
print('')
r = float(input('Discount factor: '))
CFs = list()

# receiving clients cash flows and storing in list until 'done'
print('')
print('Enter cash flows, pushing enter for each year')
print('Type "done" when finished')
print('')

while True:
    inp = input('Cash Flow: ')
    if inp == 'done':
        break
    value = float(inp)
    CFs.append(value)

print('')
print('Cash flow summary:',CFs)
print('')

# discounting function
discounted_CFs = list()
period = 1.0
for i in CFs:
    discounted = (i/((1+r)**period))
    discounted_CFs.append(discounted)
    period = period + 1
final = sum(discounted_CFs)

print('Discounted cash flow summary:',discounted_CFs)
print('')
print('The present value of cash flows is: ',final)
print('')