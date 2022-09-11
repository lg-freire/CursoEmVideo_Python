s = t = 0
while True:
    n = int(input('I will do this FOREVER unless you type in "999". Go: '))
    if n == 999:
        break
    t += 1
    s += n
print(f'Fine. You typed in {t} numbers before 999, and they add up to {s}. Now leave me alone.')
