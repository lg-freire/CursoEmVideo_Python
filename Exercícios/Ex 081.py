from time import sleep
nums = []
count = 1

while True:
    n = int(input(f'Insert value #{count}: '))
    nums.append(n)
    choice = input('Continue [Y/N]: ').strip()
    while choice not in 'yn':
        choice = input(f'''\033[31mINVALID INPUT\033[m
Continue [Y/N]: ''')
    if choice == 'n':
        print('\033[35mEXITING PROGRAM\033[m')
        break
    count += 1

nums.sort(reverse=True)
sleep(1.5)
print(f"""You inserted a total of {len(nums)} numbers.
They are, in descending order: {nums}""")

if 5 in nums:
    print(f'The number 5 was found in the #{nums.index(5)+1} position of the list.')
else:
    print('The number 5 was not detected in the list.')
