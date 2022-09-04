n = int(input('Input an integer number: '))
v = 0
for i in range(2, n):
    if n % i == 0:
        v -= 1
        print('Not a prime.')
        break
if v == 0:
    print('Prime.')
