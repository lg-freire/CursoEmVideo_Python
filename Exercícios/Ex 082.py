from time import sleep

print(f'\033[42m{"ODD/EVEN DETECTOR":^30}\033[m')
print('+' * 30)

nums, evens, odds = [], [], []
count = 1

while True:
    while True:
        try:
            nums.append(int(input(f'Insert value #{count}: ')))
            break
        except ValueError:
            print(f"""\033[31mINVALID INPUT\033[m
Please insert a number!""")
    count += 1
    choice = input('Continue [Y/N]? ')
    while choice.lower() not in 'yn':
        choice = input("""\033[31mINVALID INPUT\033[m
Continue [Y/N]? """)
    if choice == 'n':
        print('\033[35mEXITING PROGRAM\033[m')
        break

sleep(1.5)
for i in nums:
    if i % 2 == 0:
        evens.append(i)
    else:
        odds.append(i)

print(f"""The full list is \033[32m{nums}\033[m.
The even numbers are \033[34m{evens}\033[m
The odd numbers are \033[31m{odds}\033[m""")
