from time import sleep
from MyFunctions import title


def count(x, y, z):
    print(f'Count from {x} to {y} in step {z}:')
    if z == 0:
        z = 1
    if x > y and z >= 0:
        z = -z
    if y >= 0:
        for i in range(x, y+1, z):
            print(f'{i}', end=' ')
            sleep(0.4)
    else:
        for i in range(x, y-1, z):
            print(f'{i}', end=' ')
            sleep(0.4)
    print('END')
    print('-' * 30)
    sleep(1)


title('SPEEDY COUNTER', 30)
count(1, 10, 1)
count(10, 0, 2)
print('Now make your own count:')
a = int(input('START: '))
b = int(input('END: '))
c = int(input('STEP: '))
count(a, b, c)
