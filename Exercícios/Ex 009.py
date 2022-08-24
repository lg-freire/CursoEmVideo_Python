n = int(input('State a number: '))
print('Multiplication table for {}:'.format(n))
for i in range(0,11):
    print(n, 'x', i, '=', n*i)
