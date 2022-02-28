# FCC Exercises

reghr = 40
otpay = 1.5


print('')
nam = input('Enter your name: ')
print('Welcome',nam)
print('')


try:
    hours = float(input('Enter your hours: '))
    rate = float(input('Enter your rate: '))
except:
    print('Error, please enter numeric input')
    exit()

def computepay(hours,rate):
    reghr = 40
    otpay = 1.5

    print('')

    if hours > reghr:
        ot =  hours - reghr
        pay = ((reghr*rate)+(ot*(rate*otpay)))
        print('Pay = ',pay)
    else:
        pay = hours*rate
        print('Pay = ',pay)
    print('')

computepay(hours,rate)