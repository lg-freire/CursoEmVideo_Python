n = int(input('Input a number: '))
r = int(input('Input the factor: '))
count = 10
while count != 0:
    print(f'{n}', end='')
    print(' → 'if count > 1 else '', end='')
    n += r
    count -= 1
