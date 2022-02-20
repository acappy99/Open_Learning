from multiprocessing.connection import wait
import numpy as np

bored = 1

print('Hello, welcome to your world')
nam = input('What is your name ')
print('')
print('Thank you,', nam)
print('')
print('I see you are pretty bored, what do you want to do?')

while bored == 1:

    print('1 - Wanna see a bunch of numbers?')
    print('2 - Bees?')
    print('3 - Bees')
    print('4 - Nvm')

    a = input('Enter your choice: ')
    a = int(a)

    if a == 1:
        x = input('How many numbers do you want to see?')
        x = int(x)
        while x > 0:
            print(x)
            x = x - 1

    if a == 2:
        y = input('How many?')
        y = int(y)
        print('bees? '*y)

    if a == 3:
        print('bees '*10000)

    print('')
    print('Are you still bored?')
    print('0 - No')
    print('1 - Yea')
    still = input()
    bored = int(still)
    if bored == 1:
        print('')
        print('In that case..')



print('')
print('Goodbye, ',nam)
print('')

