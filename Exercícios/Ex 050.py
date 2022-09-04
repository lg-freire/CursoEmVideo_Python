s = 0
for i in range(0, 6):
    n = int(input('Enter number {}: '.format(i + 1)))
    if n % 2 == 0:
        s += n
print(f'The sum of all even numbers you presented is {s:.2f}.')
