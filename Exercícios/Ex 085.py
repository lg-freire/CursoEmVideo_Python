full = [[], []]

for i in range(1, 8):
    while True:
        try:
            n = int(input(f'Input #{i}: '))
            break
        except ValueError:
            print('''\033[31mINVALID INPUT\033[m
Introduce a numerical value.''')
    if n % 2 == 0:
        full[0].append(n)
    else:
        full[1].append(n)

print(f'''The odd numbers were {sorted(full[0])}.
The even numbers were {sorted(full[1])}.''')
