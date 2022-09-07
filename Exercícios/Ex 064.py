n, am, s = 0, -1, 0
while n != 999:
    am += 1
    s += n
    n = int(input('Type any value below 999: '))
print(f'You typed \033[34m{am}\033[m numbers below 999. They sum up to \033[31m{s}\033[m.')
