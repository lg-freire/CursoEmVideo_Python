full, odd, even = [], [], []
for i in range(1, 8):
    while True:
        try:
            n = int(input(f'Input #{i}: '))
            break
        except ValueError:
            print('''\033[31mINVALID INPUT\033[m
Introduce a numerical value.''')
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)
full.append(sorted(odd))
full.append(sorted(even))
print(f'''The odd numbers were {full[0]}.
The even numbers were {full[1]}.''')
