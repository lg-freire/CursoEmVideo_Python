from random import randint
t = ()
for i in range(0, 5):
    t += (randint(0, 100),)
print(f'Between the numbers {t}, the largest is \033[31m{max(t)}\033[m and the smallest is \033[32m{min(t)}\033[m.')
