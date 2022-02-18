
# derivative calculator

# constants
e = 2.718281828459045
selection = 1

while selection != 0:

    print('Select a function')
    print('1 - Duration based hedging')
    print('2 - CME conversion')
    print('3 - Optimal hedge')
    print('4 - Hedging using index futures')
    print('5 - Cost of carry (base case)')
    print('6 - Cost of carry w/ known yield')
    print('7 - Cost of carry w/ known income')
    print('8 - Cost of carry w/ storage cost')
    print('0 - Exit')
    selection = int(input())

    if selection == 1:
        print('')
        pval = float(input('portfolio value: '))
        pdur = float(input('portfolio duration: '))
        fval = float(input('futures value: '))
        fdur = float(input('underlying duration: '))
        ncon = (pval*pdur)/(fval*fdur)
        print('')
        print('optimal number of contracts = ',ncon)

    if selection == 2:
        print('')
        print('CME Conversion:')
        print('')
        conf = float(input('conversion factor = '))
        sprice = float(input('most recent stock price = '))
        aint = float(input('accrued interest = '))
        amt = (conf * sprice) + aint
        print('')
        print('the amount investor receives = ',amt)

    if selection == 3:
        print('')
        corr = float(input('correlation between stock and futures price changes: '))
        svar = float(input('stock price variation: '))
        fvar = float(input('futures price variation: '))
        h = corr*(svar/fvar)
        print('optimal hedge is ',h*100,"% of exposure")

    if selection == 4:
        print('')
        beta = float(input('asset beta: '))
        aval = float(input('asset value: '))
        fval = float(input('futures value: '))
        n = beta*(aval/fval)
        print('optimal number of contracts = ',n)

    if selection == 5:
        print('')
        print('Cost of carry (base case)')
        print('')
        s0 = float(input('asset price = '))
        r = float(input('r = '))
        t = float(input('t = '))
        f0 = s0 * (e**(r*t))
        print('F0 =', f0)

    if selection == 6:
        print('')
        print('Cost of carry w/ known yield')
        print('')
        s0 = float(input('asset price = '))
        r = float(input('r = '))
        q = float(input('yield = '))
        t = float(input('t = '))
        f0 = s0*(e**((r-q)*t))
        print('F0 =',f0)
    
    if selection == 7:
        print('')
        print('Cose of carry with w/ known income')
        print('')
        s0 = float(input('asset price = '))
        inc = float(input('income = '))
        r = float(input('r = '))
        t = float(input('t = '))
        f0 = (s0-inc)*(e**(r*t))
        print('F0 =',f0)
    
    if selection == 8:
        print('')
        print('Cost of carry w/ storage cost')
        print('')
        s0 = float(input('asset price = '))
        r = float(input('r = '))
        u = float(input('storage cost = '))
        t = float(input('t = '))
        f0 = (s0+u)*(e**(r*t))
        print('F0 =',f0)

    if selection == 9:
        print('')
        print('Cost of carry w/ foreign currency:')
        print('')
        s0 = float(input('asset price = '))
        rd = float(input('domestic r = '))
        rf = float(input('foreign r ='))
        t = float(input('t = '))
        f0 = s0*(e**((rd-rf)*t))
        print('F0 =',f0)

    
    print('')
