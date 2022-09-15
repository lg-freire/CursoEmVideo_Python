def title(st, x):
    print('\033[1;32m-' * x)
    print(f'{st:^{x}}')
    print('-' * x, '\033[m')


