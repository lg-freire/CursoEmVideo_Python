count = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen',
         'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty')
while True:
    try:
        n = int(input('Please input a number from 1 to 20: '))
    except ValueError:
        n = int(input("""\033[31mINVALID INPUT\033[m
Please input a number from 1 to 20: """))
    if 0 < n <= 20:
        break
    else:
        print("\033[31mINVALID INPUT\033[m")
print('-=' * 20)
print(f'You typed in the number {count[n - 1]}. Now git out.')
