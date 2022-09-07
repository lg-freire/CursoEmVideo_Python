n = int(input('Gimme a number: '))
lar, sm, over, tot = n, n, 0, 0
op = ''
while op != 'n':
    if n > lar:
        lar = n
    if n < sm:
        sm = n
    over += n
    tot += 1
    op = input('Wanna add more numbers into this? (Y/N): ').strip().lower()
    if op == 'y':
        n = int(input('Then gimme another: '))
    elif op == 'n':
        print('Aight.', end=' ')
    while op != 'n' and op != 'y':
        op = input('YES or NO, dickface (Y/N): ').strip().lower()
        if op == 'y':
            n = int(input('Then gimme another: '))
        elif op == 'n':
            print('Aight.', end=' ')
print(f'The numbers you gave me average at \033[34m{over / tot:.0f}\033[m. The largest was \033[31m{lar}\033[m and'
      f' the smallest was \033[33m{sm}\033[m.')
