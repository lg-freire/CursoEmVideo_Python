from MyFunctions import title
from time import sleep
from random import randint


def roll(li):
    print('Generating 5 random numbers: ')
    for i in range(0, 5):
        n = randint(0, 10)
        li.append(n)
        print(n, end=' ')
        sleep(.4)
    print('END')
    sleep(1.5)


def listAdd(li):
    print(f'''List of numbers: {li}
The sum its even numbers is:''', end=' ')
    s = 0
    sleep(1)
    for i in li:
        if i % 2 == 0:
            s += i
    print(s)


title('SUM OF RANDOM NUMBERS', 35)
numbers = []
roll(numbers)
listAdd(numbers)
