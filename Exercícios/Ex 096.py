from MyFunctions import title


def area(length, width):
    a = length * width
    print('-' * 30)
    print(f'The area of this terrain is \033[34m{a} m²\033[m')


title('AREA CALCULATOR', 30)
x = int(input('LENGTH (m): '))
y = int(input('WIDTH (m): '))
area(x, y)
