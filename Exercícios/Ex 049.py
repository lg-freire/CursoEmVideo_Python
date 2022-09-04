n = int(input('State a number: '))
print('Multiplication table for {}:'.format(n))
print('-=' * 10)
for i in range (1, 11):
    print('{} x {} = {}'.format(n, i, n * i))
print('-=' * 10)
