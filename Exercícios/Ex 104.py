from MyFunctions import title


def readInt(st):
    while True:
        num = input(st)
        if num.isdigit():
            break
        else:
            print("""\033[31mERROR!\033[m Input a valid number.""")
    return num


title('NUMBER READER', 25)
n = readInt('Input a number: ')
print(f'You typed the number {n}.')
