c, n = 0, 0
for i in range(1, 500, 2):
    if i % 3 == 0:
        c += i
        n += 1
print(f'The sum of the {n} numbers is {c}.')
