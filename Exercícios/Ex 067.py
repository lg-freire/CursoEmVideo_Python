while True:
    n = int(input('Math table for: '))
    if n < 0:
        print('\033[31mPROGRAM ABORTED.\033[m')
        break
    for i in range(1, 11):
        print(f'{n} x {i} = {n*i}')
    print('-=-' * 10)
