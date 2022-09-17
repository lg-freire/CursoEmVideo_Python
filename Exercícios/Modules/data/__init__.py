def validate(st='Value'):
    while True:
        x = input(st).replace(',', '.')
        if x.isalpha() or x.strip() == '':
            print('''\033[1;31mINVALID INPUT\033[m
Please input a valid number.''')
        else:
            x = float(x)
            break
    return x
