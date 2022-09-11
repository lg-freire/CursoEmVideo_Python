from time import sleep
a = m = w = 0
count = 1
while True:
    print('-' * 20)
    print(f'SUBJECT REGISTRATION #{count}')
    print('-' * 20)
    while True:
        try:
            age = int(input('Subject age: '))
            break
        except ValueError:
            print("""\033[31mINVALID INPUT.\033[m
Please input a number.""")
    gen = input('Subject gender [M/F]: ').strip().lower()
    while gen != 'm' and gen != 'f':
        gen = input("""\033[31mINVALID INPUT.\033[m
Please input a valid gender: """).strip().lower()
    if age >= 18:
        a += 1
    if gen == 'm':
        m += 1
    if gen == 'f' and age <= 20:
        w += 1
    flag = input('Are there more subjects for registration [Y/N]? ').strip().lower()
    while flag != 'y' and flag != 'n':
        flag = input('Yes [Y] or No [N]: ').strip().lower()
    if flag == 'n':
        print('\033[33mPROGRAM TERMINATED.\033[m')
        break
    count += 1
sleep(1.5)
print('=' * 10)
print(f"""\033[34mEXECUTION COMPLETE.\033[m
Subjects of age: {a}
Male subjects: {m}
Female subjects under 20 years old: {w}""")
