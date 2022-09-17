from MyFunctions import title
from time import sleep


def helpSystem():
    while True:
        title('pyHELP SUPPORT FUNCTION', 100)
        st = input('What function or library would you like to know more about (END to close the program)? → ')
        if st.upper().strip() == 'END':
            print('\033[31m', '~' * 100, f'\n{"SHUTTING DOWN":^100}\n', '~' * 100, '\033[m')
            sleep(1)
            break
        title(f'ACCESSING HELP FOR THE {st} COMMAND', 100)
        print('\033[34m', end='')
        help(st)
        print('\033[m', end='')
        sleep(1)


helpSystem()
