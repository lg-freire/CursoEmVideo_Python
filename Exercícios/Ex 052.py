n = int(input('Input an integer number: '))
v = 0
for i in range(1, n+1):
    if n % i == 0:
        v += 1
        print('\033[91m', end='')
    else:
        print('\033[94m', end='')
    print(f'{i} ', end='')
print(f'\n\033[m{n} was divided a total of {v} times, ', end='')
if v == 2:
    print('it is therefore a\033[94m prime\033[m number.')
else:
    print('it is therefore\033[91m not a prime\033[m number.')
