# Time Value of Money Calculator

choice = 1

while choice > 0:
    print('1 - PV of Cash Flows')
    print('2 - PV of Perpetuity')
    print('0 - Exit')
    print('')
    choice = int(input('> '))

    if choice == 1:
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

    if choice == 2:
        print('')
        print('Present value of a perpetuity')
        print('')
        perp = float(input('Enter the cash flow that pays into perpetuity: '))
        print('')
        r = float(input('Enter the required rate: '))
        print('')
        g = (input('Enter the growth rate (or leave blank): '))
        print('')
        if g == '':
            g = 0
        g = float(g)

        value = perp/(r-g)
        print('The value of the perpetual cash flows is:',value)
        print('')

print('Goodbye')
print('')