n = int(input('First number: '))
p = int(input('Rate: '))
print(n)
for i in range(0, 9):
    print(f'{n} + {p} = {n + p}')
    n += p
print('END')
