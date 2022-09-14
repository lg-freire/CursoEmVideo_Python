from time import sleep

print(f'\033[42m{"NAME AND WEIGHT ANALYZER":^50}\033[m')
print('=' * 50)

full, partial, lightn, heavyn = [], [], [], []
heavy = light = 0
count = 1

while True:
    partial.append(input(f'Name of subject #{count}: '))
    while True:
        try:
            partial.append(float(input(f'Weight of subject #{count} (in kg): ')))
            break
        except ValueError:
            print("""\033[31mINVALID INPUT\033[m
Please input a numeric value.""")
    full.append(partial[:])
    partial.clear()
    count += 1
    choice = input('Continue [Y/N]: ')
    while choice.lower() not in 'yn':
        choice = input("""\033[31mINVALID INPUT\033[m
Continue [Y/N]? """)
    if choice == 'n':
        print('\033[34mFINALIZING PROGRAM\033[m')
        break

for i in full:
    if heavy == 0:
        heavy = light = i[1]
    else:
        if i[1] >= heavy:
            heavy = i[1]
        elif i[1] < light:
            light = i[1]
for i in full:
    if i[1] == heavy:
        heavyn.append(i[0])
    if i[1] == light:
        lightn.append(i[0])

sleep(1.5)
print('=' * 50)
print(f'''You registered a total of {len(full)} subjects.
The heaviest subject(s), \033[31m{heavyn}\033[m, weight {heavy:.1f}kg.
The lightest subject(s), \033[34m{lightn}\033[m, weight {light:.1f}kg. ''')
