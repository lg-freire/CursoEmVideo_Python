n = int(input('Input a number: '))
r = int(input('Input the factor: '))
count, tcount = 11, 0
while count != 0:
    if count > 1:
        print(f'{n}', end='')
        print(' → ' if count > 2 else ' → PAUSE', end='')
        n += r
        count -= 1
        tcount += 1
    else:
        add = int(input('''\nWould you like to continue with the progression?
Input how many more instances you'd like to see, or input 0 to exit: '''))
        if add != 0:
            count += add
        else:
            count = 0
print(f'Process finished with {tcount} readings.')
