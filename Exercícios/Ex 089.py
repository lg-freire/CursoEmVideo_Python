print(f'\033[35m{"STUDENT SCORE ANALYZER":^50}')
print('=-' * 25, '\033[m')

full, partial, names, scores = [], [], [], []
count = 1

while True:
    name = input(f'Name of student \033[32m#{count}\033[m: ')
    names.append(name)
    while True:
        try:
            n1 = int(input(f'Student #{count} first test score: '))
            break
        except ValueError:
            print('\033[31mINVALID INPUT\033[m')
    scores.append(n1)
    while True:
        try:
            n2 = int(input(f'Student #{count} second test score: '))
            break
        except ValueError:
            print('\033[31mINVALID INPUT\033[m')
    scores.append(n2)
    partial.append(names[:])
    partial.append(scores[:])
    full.append(partial[:])
    names.clear()
    scores.clear()
    partial.clear()
    count += 1
    flag = input('Continue [Y/N]: ').strip().lower()
    while flag not in 'yn':
        flag = input("""\033[31mINVALID INPUT\033[m
Continue [Y/N]: """).strip().lower()
    if flag == 'n':
        print('-=' * 25)
        break

print(f'#   Names {"Avg.":>30}')
print('-' * 40)
for c, i in enumerate(full):
    avg = (full[c][1][0] + full[c][1][1]) / 2
    print(f'{c+1}', end='   ')
    [print(i, end='') for i in full[c][0]]
    print(f'{avg:>32.1f}')
print('-' * 40)

while True:
    while True:
        try:
            choice = int(input('Show scores of which student (type 999 to close the program)? '))
            break
        except ValueError:
            print('\033[31mINVALID INPUT\033[m')
    if choice == 999:
        print('\033[34mPROGRAM TERMINATED\033[m')
        break
    print('The scores of', end=' ')
    [print(i, end=' ') for i in full[choice-1][0]]
    print(f'are {full[choice-1][1]}.')
    print('-=' * 25)
