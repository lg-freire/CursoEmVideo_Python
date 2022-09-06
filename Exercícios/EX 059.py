v1 = int(input('Input the first number: '))
v2 = int(input('Input the second number: '))
op = 0
while op != 5:
    if op == 0:
        op = int(input("""Would you like to:\033[32m
(1) Add the numbers\033[33m
(2) Multiply the numbers\033[35m
(3) Find the highest number\033[37m
(4) Input new numbers\033[31m
(5) Close the program\033[m
Your option: """))
    if op == 1:
        print(f'{v1} + {v2} = {v1+v2}')
        op = int(input('Anything else? '))
    elif op == 2:
        print(f'{v1} * {v2} = {v1*v2}')
        op = int(input('Anything else? '))
    elif op == 3:
        if v1 == v2:
            print(f"{v1} and {v2} are the same number.")
            op = int(input('Anything else? '))
        elif v1 > v2:
            print(f'{v1} is higher than {v2}.')
            op = int(input('Anything else? '))
        else:
            print(f'{v2} is higher than {v1}.')
            op = int(input('Anything else? '))
    elif op == 4:
        v1 = int(input('New first number: '))
        v2 = int(input('New second number: '))
        op = int(input('What would you like to do with these new values? '))
    elif op >= 6:
        op = int(input('Please input a valid option. '))
