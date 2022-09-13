from time import sleep

print(f'\033[36m{"NUMBER ORGANIZER":^30}')
print('-' * 30, '\033[m')
nums = []
case = 1

while True:
    n = int(input(f'Insert number #{case}: '))
    while True:
        if n in nums:
            n = int(input(f"""\033[31mINVALID INPUT\033[m Do not enter repeat values!
Insert number #{case}: """))
        else:
            nums.append(n)
            break
    case += 1
    choice = input('Continue [Y/N]: ').strip().lower()
    if choice in 'yn':
        if choice == 'n':
            print('\033[35mEXITING PROGRAM\033[m')
            break
    else:
        choice = input(f"""\033[31mINVALID INPUT\033[m
Continue [Y/N]: """)

sleep(1.5)
print(f'You inserted the numbers {sorted(nums)}')
