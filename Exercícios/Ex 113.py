def validateInt():
    while True:
        try:
            n = int(input('Type an integer number: '))
            break
        except ValueError as error:
            if error.__cause__ is None:
                print('\033[31mUser chose not to input this value\033[m')
                n = 0
                break
            else:
                print('''\033[1;31mINVALID INPUT\033[m
                Please input a valid number.''')
        except KeyboardInterrupt:
            print('\033[31mUser chose not to input this value\033[m')
            n = 0
            break
    return n


def validateFloat():
    while True:
        try:
            n = float(input('Type a floating point number: '))
            break
        except ValueError as error:
            if error.__cause__ is None:
                print('\033[31mUser chose not to input this value\033[m')
                n = 0
                break
            else:
                print('''\033[1;31mINVALID INPUT\033[m
        Please input a valid number.''')
        except KeyboardInterrupt:
            print('\033[31mUser chose not to input this value\033[m')
            n = 0
            break
    return n


n1 = validateInt()
n2 = validateFloat()
print(f'You typed the integer {n1} and the float value {n2}.')
