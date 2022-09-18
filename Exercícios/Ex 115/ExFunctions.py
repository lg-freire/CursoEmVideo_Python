from MyFunctions import title
from time import sleep


def menu(n):
    size = n
    title('MAIN MENU', size)
    print("""\033[33m1\033[m - \033[34mSee registered subjects\033[m
\033[33m2\033[m - \033[34mRegister new subject\033[m
\033[33m3\033[m - \033[34mQuit\033[m""")
    print('\033[32m-' * size, '\033[m')


def registry(st='Choice: '):
    while True:
        menu(40)
        try:
            ch = int(input(st))
            if ch == 1:
                fileRead()
            elif ch == 2:
                fileWrite()
            elif ch == 3:
                title('Exiting...', 40)
                sleep(1)
                break
            else:
                print('\033[31mINVALID INPUT\033[m')
                sleep(1)
        except ValueError:
            print('\033[31mINVALID INPUT\033[m')
            sleep(1)


def fileRead():
    print('\033[36m-' * 40)
    print('REGISTERED PEOPLE'.center(40))
    print('-' * 40, '\033[m')
    with open("name_registry.txt", 'r') as f:
        file = f.readlines()
    for line in file:
        name, age = line.strip().split(',')
        print(f'{name:30}{f"{age}"" years":10}')
    sleep(1)


def fileWrite():
    print('\033[34m-' * 40)
    print('NEW REGISTRY'.center(40))
    print('-' * 40, '\033[m')
    name = input('Name: ')
    age = input('Age: ')
    with open("name_registry.txt", 'a') as f:
        f.write(f'\n{name}, {age}')
    print(f'Registry of {name} completed.')
    sleep(1)


