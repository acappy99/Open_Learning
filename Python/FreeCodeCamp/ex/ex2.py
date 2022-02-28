# Exercise

numbers = list()

while True:
    try:
        num = input('Enter a number: ')
        if num == 'done':
            break
        else:
            num = float(num)
            numbers.append(num)
    except:
        print('Error, please enter numerical data')

print(numbers)
print('')

print('Count = ', len(numbers))
print('Sum = ', sum(numbers))
print('Max = ',max(numbers))
print('Min = ', min(numbers))
print('Average = ', (sum(numbers)/len(numbers)))
