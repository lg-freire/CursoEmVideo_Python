from time import sleep
from random import randint

lott = []

print(f'\033[32m{"LOTTERY GENERATOR":^50}\033[m')
print('=' * 50)

while True:
    try:
        times = int(input('How many games would you like to generate? '))
        break
    except ValueError:
        print('\033[31mINVALID INPUT\033[m')
print(f"== GENERATING {times} GAMES ==")

for i in range(1, times+1):
    for j in range(0, 6):
        num = randint(1, 60)
        if num not in lott:
            lott.append(num)
        else:
            j -= 1
    sleep(1)
    print(f'Game number \033[34m#{i}\033[m: {sorted(lott)}')
    lott.clear()
