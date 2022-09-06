n = int(input('Insert a number to obtain its factorial: '))
n1 = n
fac = 1
while n1 != 0:
    fac *= n1
    n1 -= 1
print(f'{n}! = {fac}')
