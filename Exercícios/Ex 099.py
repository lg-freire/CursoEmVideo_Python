from MyFunctions import title
from time import sleep


def highest(*n):
    title('Analyzing data...', 25)
    for i in n:
        print(i, end=' ')
        sleep(0.4)
    sleep(1)
    print(f'''\nA total of \033[32m{len(n)}\033[m value(s) was/were given.
The largest was \033[31m{max(n)}\033[m''')
    sleep(1)


highest(2, 9, 4, 5, 7, 1)
highest(4, 7, 0)
highest(1, 2)
highest(6, 0)
highest(0)
